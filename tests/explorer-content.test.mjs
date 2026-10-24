import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

for (const [route, examples] of [
  ['notions/cpp-01', ['component-stock', 'independent-copy']],
  ['exemple-voyant', ['reservoir-level', 'inclusive-threshold']],
]) {
  test(`${route}: complete static sheets and valid accessible relationships`, async () => {
    const html = await readFile(`dist/${route}/index.html`, 'utf8');
    for (const example of examples) assert.ok(html.includes(`data-example="${example}"`));
    assert.equal([...html.matchAll(/data-example="/g)].length, 2);
    assert.match(html, /data-fallback/);
    assert.match(html, /data-reading[^>]*role="region"[^>]*aria-label="Lecture de l’exemple"/);
    assert.match(html, /data-pagefind-ignore/);
    assert.match(html, /data-open hidden/);
    const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(match => match[1]);
    assert.equal(new Set(ids).size, ids.length, `${route}: duplicate HTML IDs`);
    for (const match of html.matchAll(/aria-(?:controls|labelledby)="([^"]+)"/g)) {
      for (const id of match[1].split(' ')) assert.ok(ids.includes(id), `Missing ARIA target ${id}`);
    }
    assert.equal([...html.matchAll(/<select[^>]*data-select/g)].length, 0, 'Single-sheet categories need no selector');
  });
}

test('the seven course diagram snapshots match their authoritative local sources', async () => {
  const pairs = [
    ['measurement-count', 'measurement-count/02-activity-observed-values'],
    ['constant-limit', 'constant-limit/01-activity-values'],
    ...['04-activity-stock', '05-activity-copy', '06-activity-reservoir', '07-activity-strict', '08-activity-inclusive']
      .map(name => [name, `example-explorer/${name}`]),
  ];
  for (const [snapshot, source] of pairs) {
    assert.deepEqual(await readFile(`public/diagrams/examples/${snapshot}.svg`),
      await readFile(`docs/architecture/diagrams/${source}.svg`));
  }
});
