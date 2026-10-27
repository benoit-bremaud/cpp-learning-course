import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFile, readdir, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const lessonPath = 'src/content/docs/notions/premiers-calculs.md';
function run(lesson = lessonPath) {
  const result = spawnSync('python3', ['tests/program-output.py', '--lesson', 'arithmetic-update', lesson], { encoding: 'utf8', timeout: 90000 });
  assert.ifError(result.error);
  return result;
}

test('actual arithmetic and literal-replacement sources meet independent C++17 contracts', () => {
  const result = run();
  assert.equal(result.status, 0, result.stderr);
  for (const key of ['arithmetic-update', 'literal-replacement']) assert.match(result.stdout, new RegExp(`PASS ${key}:`));
});

test('arithmetic evidence rejects fixed results, fake observations, broken operations and inventories', async () => {
  const text = await readFile(lessonPath, 'utf8');
  const programs = [...text.matchAll(/^```cpp wrap\n([\s\S]*?)^```/gm)].map(match => match[1]);
  const change = (index, mutate) => text.replace(programs[index], mutate(programs[index]));
  const variants = [
    ['initial', change(0, s => s.replace('int measurement_count = 2;', 'int measurement_count = 4;')), /unexpected stdout/],
    ['missing-update', change(0, s => s.replace('    measurement_count = measurement_count + 1;\n', '')), /unexpected stdout/],
    ['early-update', change(0, s => s.replace('int measurement_count = 2;', 'int measurement_count = 2; measurement_count = measurement_count + 1;')), /unexpected stdout/],
    ['wrong-addend', change(0, s => s.replace('measurement_count + 1;', 'measurement_count + 2;')), /unexpected stdout/],
    ['update-replaced', change(0, s => s.replace('measurement_count = measurement_count + 1;', 'measurement_count = 1;')), /unexpected stdout/],
    ['fake-fixed-three', change(0, s => s.replace('measurement_count = measurement_count + 1;', 'measurement_count = 3;')), /seven arithmetic\/replacement observation statements/],
    ['fake-update-observations', change(0, s => s.replace('std::cout << measurement_count;', 'std::cout << 2;').replace('std::cout << measurement_count;', 'std::cout << 3;')), /seven arithmetic\/replacement observation statements/],
    ['quoted-name', change(0, s => s.replace('std::cout << measurement_count;', 'std::cout << "measurement_count";')), /unexpected stdout/],
    ['newline', change(0, s => s.replace('std::cout << "\\n";', 'std::cout << "";')), /unexpected stdout/],
    ['stderr', change(0, s => s.replace('return 0;', 'std::cerr << "unexpected"; return 0;')), /unexpected stderr/],
    ['status', change(0, s => s.replace('return 0;', 'return 1;')), /unexpected exit status/],
    ['replacement-calculated', change(1, s => s.replace('measurement_count = 1;', 'measurement_count = measurement_count + 1;')), /unexpected stdout/],
    ['replacement-wrong-total', change(1, s => s.replace('measurement_count = 1;', 'measurement_count = 2;')), /unexpected stdout/],
    ['fake-replacement-observations', change(1, s => s.replace('std::cout << measurement_count;', '(void)measurement_count; std::cout << 2;').replace('std::cout << measurement_count;', 'std::cout << 1;')), /seven arithmetic\/replacement observation statements/],
    ['missing-marker', text.replace('<!-- example:program-arithmetic-update -->', ''), /exactly two labelled/],
    ['wrong-marker', text.replace('<!-- example:program-literal-replacement -->', '<!-- example:program-ready -->'), /unique arithmetic-update and literal-replacement/],
    ['duplicate-marker', text.replace('<!-- example:program-literal-replacement -->', '<!-- example:program-arithmetic-update -->'), /unique arithmetic-update and literal-replacement/],
    ['extra-fence', text + '\n```cpp\nint main() { return 0; }\n```\n', /exactly two labelled/],
    ['duplicate-fence', text + '\n<!-- example:program-arithmetic-update -->\n```cpp\nint main() { return 0; }\n```\n', /exactly two labelled/],
    ['incomplete-file', change(0, s => s.replace('#include <iostream>', '')), /C\+\+17 compilation failed/],
  ];
  const directory = await mkdtemp(path.join(tmpdir(), 'cpp-arithmetic-mutations-'));
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

test('arithmetic reading maps seven statements per source and extends the published progression honestly', async () => {
  const source = await readFile(lessonPath, 'utf8');
  const html = await readFile('dist/notions/premiers-calculs/index.html', 'utf8');
  const programs = [...source.matchAll(/^```cpp wrap\n([\s\S]*?)^```/gm)].map(match => match[1]);
  assert.equal(programs.length, 2);
  const keys = ['arithmetic-update', 'literal-replacement'];
  assert.deepEqual([...source.matchAll(/data-uml="([^"]+)"/g)].map(match => match[1]), keys.map(key => `program-${key}`));
  for (const [index, key] of keys.entries()) {
    assert.match(source, new RegExp(`<!-- example:program-${key} -->\\s*\x60\x60\x60cpp wrap`));
    assert.match(source, new RegExp(`\x60\x60\x60\\s*<details class="uml-panel" data-uml="program-${key}">`));
    const panel = source.match(new RegExp(`<details class="uml-panel" data-uml="program-${key}">([\\s\\S]*?)</details>`))[1];
    const mapped = [...panel.matchAll(/<code>([^<]+;)<\/code>/g)].map(match => match[1].replaceAll('&lt;', '<').replaceAll('&quot;', '"'));
    assert.deepEqual(mapped, programs[index].split('\n').map(line => line.trim()).filter(line => line.endsWith(';')));
    assert.equal([...panel.matchAll(/<tr>/g)].length, 6);
    assert.match(panel, new RegExp(`/diagrams/examples/program-${key}.svg`));
    assert.match(panel, /target="_blank" rel="noopener noreferrer"/);
    assert.ok(source.indexOf(`](/diagrams/examples/program-${key}.svg)`) < source.indexOf(`<!-- example:program-${key} -->`));
    assert.equal([...html.matchAll(new RegExp(`<img[^>]+src="/diagrams/examples/program-${key}.svg"`, 'g'))].length, 2);
  }
  assert.equal([...html.matchAll(/<table class="observable-values"/g)].length, 4);
  assert.equal([...html.matchAll(/<pre[^>]+data-language="cpp"[^>]+wrap/g)].length, 2);
  assert.doesNotMatch(html, /data-explorer/);
  assert.match(source, /\*\*Prérequis :\*\* \[CPP-01\]\(\.\.\/cpp-01\/\)/);
  assert.match(source, /Aucun exercice autonome dédié/);
  assert.doesNotMatch(source.split('---')[1], /CPP-02/);
  const previous = await readFile('src/content/docs/notions/cpp-09.md', 'utf8');
  assert.match(previous, /\*\*Suite :\*\*.*\.\.\/premiers-calculs\//);
  assert.match(await readFile('astro.config.mjs', 'utf8'), /notions\/cpp-09'[\s\S]*notions\/premiers-calculs'/);
  assert.match(html, /rel="prev" href="\/notions\/cpp-09\/"|href="\/notions\/cpp-09\/"[^>]+rel="prev"/);
  for (const filename of ['src/content/docs/parcours.md', 'src/content/docs/index.md']) {
    assert.match(await readFile(filename, 'utf8'), /six/);
  }
  let total = 0;
  for (const name of await readdir('src/content', { recursive: true })) {
    if (/\.mdx?$/.test(name)) total += [...(await readFile(path.join('src/content', name), 'utf8')).matchAll(/^```cpp/gm)].length;
  }
  assert.equal(total, 17, 'Ten complete successes, one complete rejection, six fragments');
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  assert.equal(new Set(ids).size, ids.length);
});
