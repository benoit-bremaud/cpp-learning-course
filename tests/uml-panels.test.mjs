import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readdir, readFile } from 'node:fs/promises';

async function* sources(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = `${directory}/${entry.name}`;
    if (entry.isDirectory()) yield* sources(path);
    else if (/\.mdx?$/.test(entry.name)) yield path;
  }
}

test('every teaching C++ fence has an immediate, uniquely identified UML panel', async () => {
  const keys = new Set();
  let count = 0;
  for await (const path of sources('src/content')) {
    const source = await readFile(path, 'utf8');
    for (const block of source.matchAll(/^```cpp[^\n]*\n[\s\S]*?^```\s*\n/gm)) {
      const after = source.slice(block.index + block[0].length).trimStart();
      const panel = after.match(/^<details class="uml-panel" data-uml="([^"]+)">([\s\S]*?)<\/details>/);
      assert.ok(panel, `${path}: missing immediate UML panel`);
      assert.ok(!keys.has(panel[1]), `Duplicate panel key: ${panel[1]}`);
      keys.add(panel[1]);
      assert.match(panel[2], /<summary>(Voir la conception UML|Comprendre l’écart avec la conception)<\/summary>/);
      assert.match(panel[2], /!\[[^\]]+\]\(\/diagrams\/[^)]+\.svg\)/);
      count++;
    }
  }
  assert.ok(count > 0, 'No C++ examples found');
});

test('each teaching diagram offers its original SVG in an explicitly labelled new tab', async () => {
  for await (const path of sources('src/content')) {
    const source = await readFile(path, 'utf8');
    for (const match of source.matchAll(/!\[[^\n]+\]\((\/diagrams\/[^)]+\.svg)\)/g)) {
      const after = source.slice(match.index + match[0].length).trimStart();
      assert.ok(after.startsWith(`<a href="${match[1]}" target="_blank" rel="noopener noreferrer">Ouvrir le diagramme en grand — nouvel onglet</a>`), path);
      assert.match(await readFile(`public${match[1]}`, 'utf8'), /<svg/);
    }
  }
});
