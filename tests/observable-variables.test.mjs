import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFile, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const lessonPath = 'src/content/docs/notions/cpp-01.mdx';
function run(lesson = lessonPath) {
  const result = spawnSync('python3', ['tests/program-output.py', '--lesson', 'observable-variables', lesson], { encoding: 'utf8', timeout: 90000 });
  assert.ifError(result.error);
  return result;
}

test('actual CPP-01 program observes initialization and assignment in C++17', () => {
  const result = run();
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /PASS measurement-observed:/);
});

test('observation contract rejects wrong values, fake observations and broken execution contracts', async () => {
  const text = await readFile(lessonPath, 'utf8');
  const variants = [
    ['initial', text.replace('int measurement_count = 0;', 'int measurement_count = 2;'), /unexpected stdout/],
    ['assigned', text.replace('    measurement_count = 1;', '    measurement_count = 2;'), /unexpected stdout/],
    ['early-assignment', text.replace('int measurement_count = 0;', 'int measurement_count = 0; measurement_count = 1;'), /unexpected stdout/],
    ['quoted-name', text.replace('    std::cout << measurement_count;', '    std::cout << "measurement_count";'), /unexpected stdout/],
    ['newline', text.replace('    std::cout << "\\n";', '    std::cout << "";'), /unexpected stdout/],
    ['stderr', text.replace('    return 0;', '    std::cerr << "unexpected"; return 0;'), /unexpected stderr/],
    ['status', text.replace('    return 0;', '    return 1;'), /unexpected exit status/],
    ['missing', text.replace('{/* example:program-measurement-observed */}', ''), /exactly one labelled/],
    ['wrong-marker', text.replace('{/* example:program-measurement-observed */}', '{/* example:program-ready */}'), /unique measurement-observed/],
    ['duplicate', text + '\n{/* example:program-measurement-observed */}\n```cpp\nint main() { return 0; }\n```\n', /exactly one labelled/],
    ['extra', text + '\n```cpp\nint main() { return 0; }\n```\n', /exactly one labelled/],
    ['fake-observation', text.replace('    std::cout << measurement_count;', '    (void)measurement_count; std::cout << 0;').replace('    std::cout << measurement_count;', '    std::cout << 1;'), /seven variable-observation statements/],
  ];
  const directory = await mkdtemp(path.join(tmpdir(), 'cpp-observable-mutations-'));
  try {
    for (const [name, content, diagnostic] of variants) {
      assert.notEqual(content, text, name);
      const filename = path.join(directory, `${name}.mdx`);
      await writeFile(filename, content);
      const result = run(filename);
      assert.notEqual(result.status, 0, name);
      assert.match(result.stderr, diagnostic, name);
    }
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

test('CPP-01 keeps one complete program, five mapped actions and its existing companions', async () => {
  const source = await readFile(lessonPath, 'utf8');
  const html = await readFile('dist/notions/cpp-01/index.html', 'utf8');
  assert.equal([...source.matchAll(/^```cpp/gm)].length, 1);
  assert.equal([...html.matchAll(/<table class="observable-values"/g)].length, 4);
  assert.match(source, /examples: \[component-stock, independent-copy\]/);
  assert.match(source, /\{\/\* example:program-measurement-observed \*\/\}\s*```cpp wrap/);
  assert.match(source, /```\s*<details class="uml-panel" data-uml="measurement-primary">/);
  const panel = html.match(/<details class="uml-panel" data-uml="measurement-primary">([\s\S]*?)<\/details>/);
  assert.ok(panel);
  assert.equal([...panel[1].matchAll(/<tr>/g)].length, 6);
  assert.match(panel[1], /sept instructions/);
  const authoredPanel = source.match(/<details class="uml-panel" data-uml="measurement-primary">([\s\S]*?)<\/details>/)[1];
  const mapped = [...authoredPanel.matchAll(/<code>([^<]+;)<\/code>/g)].map(match => match[1].replaceAll('&lt;', '<').replaceAll('&quot;', '"'));
  const program = source.match(/```cpp wrap\n([\s\S]*?)```/)[1];
  assert.deepEqual(mapped, program.split('\n').map(line => line.trim()).filter(line => line.endsWith(';')), 'All seven statements map in execution order');
  assert.equal([...html.matchAll(/<img[^>]+src="\/diagrams\/examples\/measurement-count.svg"/g)].length, 2);
  assert.match(panel[1], /target="_blank" rel="noopener noreferrer"/);
  assert.match(html, /<pre[^>]+data-language="cpp"[^>]+wrap/);
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(source.indexOf('](/diagrams/examples/measurement-count.svg)') < source.indexOf('{/* example:program-measurement-observed */}'));
  assert.match(source, /\[TOOL-01\]\(\.\.\/tool-01\/\)/);
  assert.match(source, /\(\.\.\/programme-minimal\/\)/);
  assert.match(source, /\(\.\.\/premiers-affichages\/\)/);
  assert.match(source, /\*\*Suite :\*\*.*\.\.\/cpp-09\//);
  const sidebar = await readFile('astro.config.mjs', 'utf8');
  assert.match(sidebar, /notions\/programme-minimal'[\s\S]*notions\/premiers-affichages'[\s\S]*notions\/cpp-01'[\s\S]*notions\/cpp-09'/);
});
