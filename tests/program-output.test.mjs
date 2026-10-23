import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { readFile, mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

const lessonPath = 'src/content/docs/notions/programme-minimal.md';
function run(lesson = lessonPath) {
  const result = spawnSync('python3', ['tests/program-output.py', lesson], { encoding: 'utf8', timeout: 90000 });
  assert.ifError(result.error);
  return result;
}

test('actual Ready and Silent lesson excerpts compile as C++17 and meet exact observations', () => {
  const result = run();
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /PASS ready:/);
  assert.match(result.stdout, /PASS silent:/);
});

test('program checks detect newline, stderr, status and excerpt-inventory regressions', async () => {
  const text = await readFile(lessonPath, 'utf8');
  const variants = [
    ['newline', text.replace('std::cout << "Ready\\n";', 'std::cout << "Ready";'), /unexpected stdout/],
    ['stderr', text.replace('std::cout << "Ready\\n";', 'std::cout << "Ready\\n"; std::cerr << "unexpected";'), /unexpected stderr/],
    ['status', text.replace('return 0;', 'return 1;'), /unexpected exit status/],
    ['missing', text.replace('<!-- example:program-ready -->', ''), /exactly two labelled/],
    ['duplicate', text.replace('<!-- example:program-silent -->', '<!-- example:program-ready -->'), /unique ready and silent/],
    ['extra', text + '\n```cpp\nint main() { return 0; }\n```\n', /exactly two labelled/],
  ];
  const directory = await mkdtemp(path.join(tmpdir(), 'cpp-program-mutations-'));
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

test('built first-program lesson preserves two primary models and exact card mappings', async () => {
  const html = await readFile('dist/notions/programme-minimal/index.html', 'utf8');
  assert.equal([...html.matchAll(/<details class="uml-panel"/g)].length, 2);
  assert.equal([...html.matchAll(/<pre[\s>]/g)].length, 3, 'Two C++ programs and one text output');
  assert.doesNotMatch(html, /data-explorer|premiers-affichages/);
  for (const key of ['ready', 'silent']) {
    const panel = html.match(new RegExp(`<details class="uml-panel" data-uml="program-${key}">([\\s\\S]*?)</details>`));
    assert.ok(panel, key);
    assert.match(panel[1], new RegExp(`/diagrams/examples/program-${key}\\.svg`));
    assert.match(panel[1], /<table>/);
    assert.equal([...html.matchAll(new RegExp(`<img[^>]+src="/diagrams/examples/program-${key}\\.svg"`, 'g'))].length, 2);
  }
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
  assert.equal(new Set(ids).size, ids.length);
  assert.match(html, /data-uml="program-ready"[\s\S]*std::cout[\s\S]*return 0;/);
  const sidebar = await readFile('astro.config.mjs', 'utf8');
  assert.match(sidebar, /notions\/tool-01'[\s\S]*notions\/programme-minimal'[\s\S]*notions\/cpp-01'/);
  const tool = await readFile('src/content/docs/notions/tool-01.md', 'utf8');
  assert.match(tool, /\*\*Suite disponible :\*\*.*\(\.\.\/programme-minimal\/\)/);
  const variables = await readFile('src/content/docs/notions/cpp-01.mdx', 'utf8');
  assert.match(variables, /\*\*Prérequis :\*\*.*\(\.\.\/programme-minimal\/\)/);
});
