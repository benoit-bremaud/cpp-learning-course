import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFile, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const lessonPath = 'src/content/docs/notions/premiers-affichages.md';
function run(lesson = lessonPath) {
  const result = spawnSync('python3', ['tests/program-output.py', '--lesson', 'ordered-output', lesson], { encoding: 'utf8', timeout: 90000 });
  assert.ifError(result.error);
  return result;
}

test('actual ordered, reversed and joined programs meet their independent C++17 contracts', () => {
  const result = run();
  assert.equal(result.status, 0, result.stderr);
  for (const key of ['ordered', 'reversed', 'joined']) assert.match(result.stdout, new RegExp(`PASS ${key}:`));
});

test('ordered-output checks reject order, space, newline, diagnostic, status and inventory mutations', async () => {
  const text = await readFile(lessonPath, 'utf8');
  const variants = [
    ['order', text.replace('std::cout << "Program started\\n";\n    std::cout << "Program finished\\n";', 'std::cout << "Program finished\\n";\n    std::cout << "Program started\\n";'), /unexpected stdout/],
    ['space', text.replace('std::cout << "System ";', 'std::cout << "System";'), /unexpected stdout/],
    ['newline', text.replace('std::cout << "ready\\n";', 'std::cout << "ready";'), /unexpected stdout/],
    ['stderr', text.replace('    return 0;', '    std::cerr << "unexpected"; return 0;'), /unexpected stderr/],
    ['status', text.replace('    return 0;', '    return 1;'), /unexpected exit status/],
    ['missing', text.replace('<!-- example:program-ordered -->', ''), /exactly three labelled/],
    ['duplicate', text.replace('<!-- example:program-reversed -->', '<!-- example:program-ordered -->'), /unique ordered, reversed and joined/],
    ['extra', text + '\n```cpp\nint main() { return 0; }\n```\n', /exactly three labelled/],
  ];
  const directory = await mkdtemp(path.join(tmpdir(), 'cpp-ordered-mutations-'));
  try {
    for (const [name, content, diagnostic] of variants) {
      assert.notEqual(content, text, `Mutation must change source: ${name}`);
      const filename = path.join(directory, `${name}.md`);
      await writeFile(filename, content);
      const result = run(filename);
      assert.notEqual(result.status, 0, `Mutation must fail: ${name}`);
      assert.match(result.stderr, diagnostic, name);
    }
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

test('built ordered-output lesson preserves three adjacent mappings and published progression', async () => {
  const source = await readFile(lessonPath, 'utf8');
  const html = await readFile('dist/notions/premiers-affichages/index.html', 'utf8');
  assert.equal([...source.matchAll(/^```cpp/gm)].length, 3);
  assert.equal([...html.matchAll(/<details class="uml-panel"/g)].length, 3);
  assert.doesNotMatch(html, /data-explorer/);
  assert.equal([...html.matchAll(/<pre[^>]+data-language="cpp"[^>]+wrap/g)].length, 3, 'All three C++ blocks reflow at narrow widths');
  const mappedInstructions = {
    ordered: ['std::cout << "Program started\\n";', 'std::cout << "Program finished\\n";', 'return 0;'],
    reversed: ['std::cout << "Program finished\\n";', 'std::cout << "Program started\\n";', 'return 0;'],
    joined: ['std::cout << "System ";', 'std::cout << "ready\\n";', 'return 0;'],
  };
  for (const key of ['ordered', 'reversed', 'joined']) {
    assert.match(source, new RegExp(`<!-- example:program-${key} -->\\s*\x60\x60\x60cpp[\\s\\S]*?\x60\x60\x60\\s*<details class="uml-panel" data-uml="program-${key}">`));
    const panel = html.match(new RegExp(`<details class="uml-panel" data-uml="program-${key}">([\\s\\S]*?)</details>`));
    assert.ok(panel, key);
    assert.equal([...panel[1].matchAll(/<tr>/g)].length, 4, 'Header and three mapped actions');
    assert.match(panel[1], /return 0;/);
    assert.equal([...html.matchAll(new RegExp(`<img[^>]+src="/diagrams/examples/program-${key}\\.svg"`, 'g'))].length, 2);
    assert.match(panel[1], /target="_blank" rel="noopener noreferrer"/);
    const authoredPanel = source.match(new RegExp(`<details class="uml-panel" data-uml="program-${key}">([\\s\\S]*?)</details>`));
    assert.deepEqual([...authoredPanel[1].matchAll(/\| `([^`]+)` \|/g)].map(match => match[1]), mappedInstructions[key]);
    assert.ok(source.indexOf(`](/diagrams/examples/program-${key}.svg)`) < source.indexOf(`<!-- example:program-${key} -->`), 'Primary model precedes its program');
  }
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  assert.equal(new Set(ids).size, ids.length);
  const sidebar = await readFile('astro.config.mjs', 'utf8');
  assert.match(sidebar, /notions\/programme-minimal'[\s\S]*notions\/premiers-affichages'[\s\S]*notions\/cpp-01'/);
  assert.match(html, /href="[^\"]*programme-minimal\//);
  assert.match(html, /href="[^\"]*cpp-01\//);
  const progression = await readFile('src/content/docs/parcours.md', 'utf8');
  assert.match(progression, /Les cinq premières étapes/);
  assert.match(progression, /\(\.\.\/notions\/premiers-affichages\/\)/);
});
