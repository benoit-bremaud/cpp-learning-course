import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve('dist');
const base = '/cpp-learning-course/';
async function pages(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const groups = await Promise.all(entries.map(async (entry) => {
    const name = path.join(dir, entry.name);
    return entry.isDirectory() ? pages(name) : name.endsWith('.html') ? [name] : [];
  }));
  return groups.flat();
}

test('built reader keeps all local navigation and assets inside the project base', async () => {
  const files = await pages(root);
  assert.ok(files.length >= 7, 'Expected the course pages and fallback');
  for (const file of files) {
    const html = await readFile(file, 'utf8');
    assert.match(html, /lang="fr"/);
    const current = new URL(base + path.relative(root, file).replace(/index\.html$/, ''), 'https://course.test');
    for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
      const url = new URL(match[1].replaceAll('&amp;', '&'), current);
      if (url.origin !== current.origin) continue;
      assert.ok(url.pathname.startsWith(base), `${file}: outside base: ${url}`);
      let target = path.join(root, decodeURIComponent(url.pathname.slice(base.length)));
      const info = await stat(target).catch(() => null);
      assert.ok(info, `${file}: missing ${url}`);
      if (info.isDirectory()) target = path.join(target, 'index.html');
      const content = await readFile(target);
      if (url.hash && target.endsWith('.html')) {
        const id = decodeURIComponent(url.hash.slice(1));
        assert.ok(content.toString().includes(`id="${id}"`), `${file}: missing anchor ${id}`);
      }
    }
  }
});

test('production search index exists and practice availability is explicit', async () => {
  await stat(path.join(root, 'pagefind/pagefind.js'));
  const practice = await readFile(path.join(root, 'pratique/index.html'), 'utf8');
  assert.match(practice, /premier exemple de référence est publié/);
  const example = await readFile(path.join(root, 'exemple-voyant/index.html'), 'utf8');
  assert.match(example, /6f6da4c440153c0709e35b823a3ef5b85c6b6b68/);
  await stat(path.join(root, 'diagrams/threshold-indicator.svg'));
  assert.match(practice, /https:\/\/github.com\/benoit-bremaud\/cpp-learning/);
});
