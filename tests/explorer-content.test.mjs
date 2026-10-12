import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

test('pilot output contains complete fallback sheets and valid dialog relationships', async () => {
  for (const [route, examples] of [
    ['notions/cpp-01', ['component-stock', 'independent-copy']],
    ['notions/premieres-expressions', ['empty-tray', 'independent-copy']],
    ['exemple-voyant', ['reservoir-level', 'inclusive-threshold']],
  ]) {
    const html = await readFile(`dist/${route}/index.html`, 'utf8');
    for (const example of examples) assert.ok(html.includes(`data-example="${example}"`));
    assert.equal([...html.matchAll(/data-example="/g)].length, 2);
    assert.match(html, /data-fallback/);
    assert.match(html, /data-pagefind-ignore/);
    assert.match(html, /data-open hidden/);
    const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
    assert.equal(new Set(ids).size, ids.length, `${route}: duplicate HTML IDs`);
    for (const match of html.matchAll(/aria-(?:controls|labelledby)="([^"]+)"/g)) {
      for (const id of match[1].split(' ')) assert.ok(ids.includes(id), `Missing ARIA target ${id}`);
    }
  }
});
