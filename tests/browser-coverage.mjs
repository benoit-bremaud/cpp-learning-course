/** Run real-DOM interaction and WCAG checks, mapping V8 coverage to authored TypeScript. */
import assert from 'node:assert/strict';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { createServer } from 'node:http';
import path from 'node:path';
import { chromium } from 'playwright';
import ts from 'typescript';
import v8toIstanbul from 'v8-to-istanbul';

const output = path.resolve('coverage');
await mkdir(output, { recursive: true });
const scripts = new Map();
for (const name of ['example-explorer', 'uml-cards']) {
  const filename = path.resolve(`src/scripts/${name}.ts`);
  const source = await readFile(filename, 'utf8');
  const { outputText } = ts.transpileModule(source, {
    fileName: filename,
    compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext, inlineSourceMap: true, inlineSources: true },
  });
  scripts.set(`/__coverage/${name}.js`, { filename, source: outputText });
}
const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url, 'http://localhost');
    const instrumented = scripts.get(url.pathname);
    if (instrumented) {
      response.setHeader('Content-Type', 'text/javascript');
      response.end(instrumented.source);
      return;
    }
    let filename = path.resolve('dist', `.${decodeURIComponent(url.pathname)}`);
    assert.ok(filename.startsWith(path.resolve('dist') + path.sep));
    if (url.pathname.endsWith('/')) filename += '/index.html';
    let content = await readFile(filename);
    if (filename.endsWith('.html')) {
      // Production HTML and styles stay real; only our two module entrypoints are replaced
      // with the same TypeScript transpiled with source maps for line measurement.
      content = content.toString().replace(/<script[^>]+src="[^"]*(?:CourseFooter|ExampleExplorer)[^"]*"[^>]*><\/script>/g, '');
      content += `<script type="module">
        import { initializeExplorers } from '/__coverage/example-explorer.js';
        import { initializeUmlCards } from '/__coverage/uml-cards.js';
        window.enhance = () => { initializeExplorers(); initializeUmlCards(); };
        window.enhance();
      </script>`;
    }
    const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.wasm': 'application/wasm' };
    response.setHeader('Content-Type', mime[path.extname(filename)] || 'application/octet-stream');
    response.end(content);
  } catch {
    response.writeHead(404).end();
  }
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
const base = `http://127.0.0.1:${server.address().port}`;
const browser = await chromium.launch(process.env.COURSE_BROWSER_EXECUTABLE
  ? { executablePath: process.env.COURSE_BROWSER_EXECUTABLE }
  : { channel: 'chrome' });
const page = await browser.newPage();
const failures = [];
page.on('pageerror', error => failures.push(error.message));
await page.coverage.startJSCoverage({ resetOnNavigation: false });
const axe = await readFile('node_modules/axe-core/axe.min.js', 'utf8');
const accessibility = [];
const collectedCoverage = [];
async function checkAccessibility(label) {
  // Scan the settled top layer, including cards retained briefly for their exit fade.
  await page.waitForFunction(() => [...document.querySelectorAll('.uml-card')].every(el =>
    el.matches(':popover-open') ? getComputedStyle(el).opacity === '1' : getComputedStyle(el).display === 'none'));
  await page.addScriptTag({ content: axe });
  const result = await page.evaluate(async () => window.axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] } }));
  // axe's DOM stacking analysis can misorder a native top-layer popover and code beneath it.
  // Resolve only that exact incomplete case, retaining the original diagnostics and checking
  // the browser's real hit order plus the opaque computed colors with axe's contrast formula.
  const contrastChecks = [];
  const unresolved = [];
  for (const item of result.incomplete.filter(item => ['serious', 'critical'].includes(item.impact))) {
    if (item.id !== 'color-contrast' || item.nodes.some(node =>
      !node.any.length || node.any.some(check => check.data?.messageKey !== 'bgOverlap'))) {
      unresolved.push(item.id); continue;
    }
    for (const node of item.nodes) {
      const measurement = await page.evaluate(selector => {
        const el = document.querySelector(selector);
        const card = el?.closest('.uml-card:popover-open');
        if (!card || getComputedStyle(card).opacity !== '1') return null;
        const foreground = new window.axe.commons.color.Color();
        foreground.parseString(getComputedStyle(el).color);
        let background;
        for (let ancestor = el; ancestor; ancestor = ancestor.parentElement) {
          const style = getComputedStyle(ancestor);
          if (style.opacity !== '1' || style.backgroundImage !== 'none') return null;
          const color = new window.axe.commons.color.Color();
          color.parseString(style.backgroundColor);
          if (color.alpha === 1) { background = color; break; }
          if (color.alpha !== 0 || ancestor === card) return null;
        }
        if (!background) return null;
        const rect = el.getBoundingClientRect();
        const hit = document.elementFromPoint(rect.x + rect.width / 2, rect.y + rect.height / 2);
        if (!hit || !el.contains(hit)) return null;
        return { selector, ratio: window.axe.commons.color.getContrast(background, foreground), foreground: getComputedStyle(el).color, opaqueBackgroundVerified: true, topLayerHitVerified: true };
      }, node.target[0]);
      if (!measurement || measurement.ratio < 4.5) unresolved.push(node.target);
      else contrastChecks.push(measurement);
    }
  }
  accessibility.push({ label, violations: result.violations, incomplete: result.incomplete, contrastChecks });
  assert.deepEqual(result.violations.map(item => ({ id: item.id, nodes: item.nodes.map(node => node.target) })), [], label);
  assert.deepEqual(unresolved, [], `${label}: unresolved serious accessibility checks`);
}
let completed = false;
try {
  for (const route of ['/notions/cpp-01/', '/exemple-voyant/']) {
    await page.goto(base + route);
    await page.waitForSelector('[data-ready]');
    await checkAccessibility(`${route}: course`);
    await page.locator('[data-open]').click();
    await checkAccessibility(`${route}: dialog`);
    for (const category of [0, 1]) {
      const tab = page.getByRole('tab').nth(category);
      await tab.click();
      for (const key of ['ArrowRight', 'ArrowLeft', 'End', 'Home', 'ArrowLeft']) await tab.press(key);
      await tab.click();
      for (const trigger of await page.locator('dialog .uml-trigger:visible').all()) {
        await trigger.click();
        await page.waitForSelector('.uml-card:popover-open[data-positioned]');
        await checkAccessibility(`${route}: card ${category}`);
        await page.setViewportSize({ width: 390, height: 844 });
        await page.locator('.uml-card:popover-open .uml-close').click();
        await trigger.click();
        await page.locator('.uml-card:popover-open .uml-close').press('Escape');
        assert.equal(await trigger.evaluate(el => el === document.activeElement), true);
        await page.setViewportSize({ width: 1440, height: 1000 });
      }
    }
    await page.locator('[data-reading]').focus();
    await page.keyboard.press('Shift+Tab');
    for (let i = 0; i < 20; i++) await page.keyboard.press('Tab');
    await page.keyboard.press('Escape');
    await page.locator('[data-open]').click();
    await page.locator('[data-close]').click();
    // Add a real two-sheet selector without publishing additional teaching material.
    await page.evaluate(() => {
      const root = document.querySelector('[data-explorer]');
      delete root.dataset.ready;
      const fallback = root.querySelector('[data-fallback]');
      for (const panel of root.querySelectorAll('[data-panel]')) fallback.append(panel);
      const panel = fallback.querySelector('[data-panel]');
      const article = document.createElement('article');
      article.dataset.example = 'second';
      article.innerHTML = '<h3>Second fixture</h3><details><summary>Fixture</summary><a href="#">Hidden control</a></details>';
      panel.append(article);
      const label = document.createElement('label');
      label.className = 'example-selector';
      label.textContent = 'Fixture';
      const select = document.createElement('select');
      select.append(new Option('First', panel.querySelector('article').dataset.example), new Option('Second', 'second'));
      label.append(select); panel.prepend(label);
      window.enhance(); window.enhance();
    });
    await page.locator('[data-open]').click();
    const selector = page.locator('dialog select');
    await selector.focus();
    await selector.selectOption('second');
    assert.equal(await page.locator('dialog article:visible h3').textContent(), 'Second fixture');
    assert.equal(await selector.evaluate(el => el === document.activeElement), true);
    for (let i = 0; i < 12; i++) await page.keyboard.press('Tab');
    await page.locator('[data-close]').click();
    collectedCoverage.push(...await page.coverage.stopJSCoverage());
    await page.coverage.startJSCoverage({ resetOnNavigation: false });
  }
  await page.goto(base + '/notions/cpp-09/');
  await page.waitForSelector('[data-card-ready]');
  for (const trigger of await page.locator('.uml-trigger').all()) {
    await trigger.focus(); await trigger.press('Enter');
    assert.equal(await page.locator('.uml-card:popover-open').count(), 1);
  }
  await page.locator('.uml-card:popover-open .uml-close').click();
  const animation = await page.locator('.uml-trigger').first().evaluate(async trigger => {
    if (!(trigger instanceof HTMLButtonElement)) throw new Error('Expected a UML button');
    const card = trigger.popoverTargetElement;
    const frames = [];
    trigger.click();
    const start = performance.now();
    while (performance.now() - start < 360) {
      await new Promise(requestAnimationFrame);
      const style = getComputedStyle(card); const rect = card.getBoundingClientRect();
      frames.push({ opacity: Number(style.opacity), visible: style.visibility === 'visible', x: rect.x, y: rect.y });
    }
    card.querySelector('.uml-close').click();
    const closing = []; const end = performance.now();
    while (performance.now() - end < 220) {
      await new Promise(requestAnimationFrame);
      const style = getComputedStyle(card);
      closing.push({ opacity: Number(style.opacity), display: style.display });
    }
    return { frames, closing };
  });
  const visibleFrames = animation.frames.filter(frame => frame.visible && frame.opacity > 0);
  assert.ok(visibleFrames.length > 0);
  assert.ok(visibleFrames.some(frame => frame.opacity < 1), 'Opening opacity must fade');
  assert.ok(Math.max(...visibleFrames.map(frame => frame.x)) - Math.min(...visibleFrames.map(frame => frame.x)) < 1);
  assert.ok(Math.max(...visibleFrames.map(frame => frame.y)) - Math.min(...visibleFrames.map(frame => frame.y)) < 1);
  assert.ok(animation.closing.some(frame => frame.opacity > 0 && frame.opacity < 1 && frame.display !== 'none'));
  assert.equal(animation.closing.at(-1).display, 'none');
  // Feature detection and missing markup must leave usable content rather than throw.
  await page.evaluate(() => {
    const malformed = document.createElement('section');
    malformed.dataset.explorer = '';
    malformed.innerHTML = '<details class="uml-panel">Missing summary fixture</details>';
    document.body.append(malformed);
    window.enhance();
    const showModal = HTMLDialogElement.prototype.showModal;
    delete HTMLDialogElement.prototype.showModal;
    window.enhance(); HTMLDialogElement.prototype.showModal = showModal;
    const showPopover = HTMLElement.prototype.showPopover;
    delete HTMLElement.prototype.showPopover;
    window.enhance(); HTMLElement.prototype.showPopover = showPopover;
  });
  assert.deepEqual(failures, []);
  completed = true;
} finally {
  const coverage = [...collectedCoverage, ...await page.coverage.stopJSCoverage()];
  const result = {};
  for (const entry of coverage) {
    if (!entry.url.startsWith(base + '/__coverage/')) continue;
    const script = scripts.get(new URL(entry.url).pathname);
    if (!script) continue;
    const converter = v8toIstanbul(script.filename.replace(/\.ts$/, '.js'), 0, { source: entry.source });
    await converter.load();
    converter.applyCoverage(entry.functions);
    for (const [filename, data] of Object.entries(converter.toIstanbul())) {
      if (!result[filename]) result[filename] = data;
      else {
        for (const [key, count] of Object.entries(data.s)) result[filename].s[key] += count;
      }
    }
  }
  let lcov = '';
  let covered = 0; let total = 0;
  for (const [filename, data] of Object.entries(result)) {
    lcov += `TN:\nSF:${filename}\n`;
    for (const [key, location] of Object.entries(data.statementMap)) {
      const hits = data.s[key];
      lcov += `DA:${location.start.line},${hits}\n`;
      total++; if (hits > 0) covered++;
    }
    lcov += 'end_of_record\n';
  }
  await writeFile(path.join(output, 'lcov.info'), lcov);
  await writeFile(path.join(output, 'browser.json'), JSON.stringify(result, null, 2));
  await writeFile(path.join(output, 'accessibility.json'), JSON.stringify(accessibility, null, 2));
  await browser.close(); await new Promise(resolve => server.close(resolve));
  assert.equal(Object.keys(result).length, 2, 'Both authored interaction modules must be measured');
  const percentage = 100 * covered / total;
  console.log(`Browser TypeScript line coverage: ${covered}/${total} = ${percentage.toFixed(2)}%`);
  if (completed) assert.ok(percentage >= 80, 'Browser coverage must meet the 80% floor');
}
