import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFile, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const lessonPath = 'src/content/docs/notions/cpp-09.md';
function run(lesson = lessonPath) {
  const result = spawnSync('python3', ['tests/constant-limit.py', lesson], { encoding: 'utf8', timeout: 90000 });
  assert.ifError(result.error);
  return result;
}

test('actual CPP-09 sources run or reject under their independent C++17 contracts', () => {
  const result = run();
  assert.equal(result.status, 0, result.stderr);
  for (const key of ['constant-stable', 'constant-rejected', 'constant-wrong']) assert.match(result.stdout, new RegExp(`PASS ${key}:`));
});

test('constant contracts reject false observations, malformed rejection and changed inventories', async () => {
  const text = await readFile(lessonPath, 'utf8');
  const rejected = text.match(/<!-- example:program-constant-rejected -->\s*```cpp wrap\n([\s\S]*?)```/)[1];
  const changeRejected = change => text.replace(rejected, change(rejected));
  const variants = [
    ['initial-count', text.replace('int measurement_count = 0;', 'int measurement_count = 2;'), /unexpected stdout/],
    ['assigned-count', text.replace('    measurement_count = 1;', '    measurement_count = 2;'), /unexpected stdout/],
    ['missing-update', text.replace('    measurement_count = 1;\n', ''), /unexpected stdout/],
    ['moved-update', text.replace('int measurement_count = 0;', 'int measurement_count = 0; measurement_count = 1;'), /unexpected stdout/],
    ['required-limit', text.replace('const int measurement_limit = 3;', 'const int measurement_limit = 4;'), /unexpected stdout/],
    ['wrong-limit', text.replace('const int measurement_limit = 30;', 'const int measurement_limit = 3;'), /unexpected stdout/],
    ['missing-const', text.replace('const int measurement_limit = 3;', 'int measurement_limit = 3;'), /twelve const\/variable-observation/],
    ['quoted-name', text.replace('std::cout << measurement_limit;', 'std::cout << "measurement_limit";'), /unexpected stdout/],
    ['newline', text.replace('std::cout << "\\n";', 'std::cout << "";'), /unexpected stdout/],
    ['stderr', text.replace('    return 0;', '    std::cerr << "unexpected"; return 0;'), /unexpected stderr/],
    ['status', text.replace('    return 0;', '    return 1;'), /unexpected exit status/],
    ['fake-limit', text.replace('std::cout << measurement_limit;', '(void)measurement_limit; std::cout << 3;').replace('std::cout << measurement_limit;', 'std::cout << 3;'), /twelve const\/variable-observation/],
    ['fake-count', text.replace('std::cout << measurement_count;', '(void)measurement_count; std::cout << 0;').replace('std::cout << measurement_count;', 'std::cout << 1;'), /twelve const\/variable-observation/],
    ['invalid-made-valid', changeRejected(s => s.replace('const int', 'int')), /expected compilation rejection/],
    ['invalid-unrelated-header', changeRejected(s => s.replace('#include <iostream>', '')), /rejection control must compile/],
    ['invalid-unrelated-syntax', changeRejected(s => s.replace('return 0;', 'return broken;')), /rejection control must compile/],
    ['invalid-extra-fault', changeRejected(s => s.replace('measurement_limit = 4;', 'measurement_limit = 4; missing = 1;')), /rejection control must compile/],
    ['invalid-wrong-assignment', changeRejected(s => s.replace('measurement_limit = 4;', 'measurement_limit = 5;')), /unexpected stdout/],
    ['missing-marker', text.replace('<!-- example:program-constant-stable -->', ''), /exactly three labelled/],
    ['wrong-marker', text.replace('program-constant-wrong', 'program-ready'), /unique stable\/rejected\/wrong/],
    ['duplicate-marker', text.replace('program-constant-wrong', 'program-constant-stable'), /unique stable\/rejected\/wrong/],
    ['extra-fence', text + '\n```cpp\nint main() { return 0; }\n```\n', /exactly three labelled/],
  ];
  const directory = await mkdtemp(path.join(tmpdir(), 'cpp-constant-mutations-'));
  try {
    for (const [name, content, diagnostic] of variants) {
      assert.notEqual(content, text, name);
      const filename = path.join(directory, `${name}.md`);
      await writeFile(filename, content);
      const result = run(filename);
      assert.notEqual(result.status, 0, name);
      assert.match(result.stderr, diagnostic, name);
    }
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

test('CPP-09 maps every statement and distinguishes actual wrong behavior from rejected compilation', async () => {
  const source = await readFile(lessonPath, 'utf8');
  const html = await readFile('dist/notions/cpp-09/index.html', 'utf8');
  assert.equal([...source.matchAll(/^```cpp wrap/gm)].length, 3);
  const programs = [...source.matchAll(/^```cpp wrap\n([\s\S]*?)^```/gm)].map(match => match[1]);
  const panels = [...source.matchAll(/<details class="uml-panel" data-uml="([^"]+)">([\s\S]*?)<\/details>/g)];
  assert.deepEqual(panels.map(panel => panel[1]), ['constant-valid', 'constant-rejected', 'constant-wrong']);
  for (const [index, panel] of panels.entries()) {
    const mapped = [...panel[2].matchAll(/<code>([^<]+;)<\/code>/g)].map(match => match[1].replaceAll('&lt;', '<').replaceAll('&quot;', '"'));
    assert.deepEqual(mapped, programs[index].split('\n').map(line => line.trim()).filter(line => line.endsWith(';')));
    const rendered = html.match(new RegExp(`<details class="uml-panel" data-uml="${panel[1]}">([\\s\\S]*?)</details>`))[1];
    assert.equal([...rendered.matchAll(/<tr>/g)].length, index === 1 ? 6 : 7);
    assert.match(source, new RegExp('```\\s*<details class="uml-panel" data-uml="'+panel[1]+'">'));
    assert.match(panel[2], /target="_blank" rel="noopener noreferrer"/);
  }
  assert.match(panels[1][2], /Conception attendue de référence/);
  assert.match(panels[1][2], /non exécut/);
  assert.match(panels[2][2], /comportement réel erroné/);
  assert.match(panels[2][2], /constant-wrong-limit.svg/);
  assert.equal([...html.matchAll(/<table class="observable-values"/g)].length, 4);
  assert.match(html, /data-language="cpp"[^>]*wrap/);
  assert.match(source, /\[CPP-01\]\(\.\.\/cpp-01\/\)/);
  assert.match(source, /GCC 15\.2\.0/);
  assert.match(source, /exercice autonome à venir/);
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  assert.equal(new Set(ids).size, ids.length);
});
