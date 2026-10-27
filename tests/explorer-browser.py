"""Exercise production output in installed browser engines; save local QA screenshots.

Requires Python Playwright. Set COURSE_BROWSER_ENGINE and COURSE_BROWSER_EXECUTABLE
for an installed engine. Run after npm test. The server binds only to loopback.
"""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
import json
import os
from playwright.sync_api import sync_playwright, expect


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


artifacts = Path(os.environ.get('COURSE_QA_DIR', '/tmp/cpp-course-pilot-qa'))
artifacts.mkdir(parents=True, exist_ok=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(Path('dist').resolve())))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
engine = os.environ.get('COURSE_BROWSER_ENGINE', 'chromium')
executable = os.environ.get('COURSE_BROWSER_EXECUTABLE', '/usr/bin/google-chrome')
errors = []
diagram_measurements = []
try:
    with sync_playwright() as pw:
        browser = getattr(pw, engine).launch(executable_path=executable)
        for width, height in [(1440, 1000), (768, 1024), (390, 844), (320, 640)]:
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
            page.on('response', lambda response: errors.append(f'HTTP {response.status}: {response.url}') if response.status >= 400 else None)
            for route in ['/notions/cpp-01/', '/exemple-voyant/']:
                page.goto(base + route)
                page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
                # Regression: the paper spans the content, but the SVG must never be upscaled.
                for diagram in page.locator('img[src^="/diagrams/"]:visible').all():
                    assert diagram.evaluate('el => el.getBoundingClientRect().width <= el.naturalWidth + 1')
                    assert diagram.evaluate('el => Math.abs(el.parentElement.getBoundingClientRect().width - el.parentElement.parentElement.getBoundingClientRect().width) < 2')
                if route == '/notions/cpp-01/':
                    for table in page.locator('table.observable-values:visible').all():
                        assert table.evaluate('el => el.scrollWidth <= el.clientWidth + 1')
                    trigger = page.locator('[data-uml="measurement-primary"] .uml-trigger')
                    trigger.focus()
                    trigger.press('Enter')
                    card = page.locator('.uml-card:popover-open')
                    expect(card).to_have_css('opacity', '1')
                    assert card.locator('tr').count() == 6
                    assert card.locator('table').evaluate('el => el.scrollWidth <= el.clientWidth + 1')
                    expect(card.locator('img')).to_have_attribute('src', '/diagrams/examples/measurement-count.svg')
                    expect(card).to_have_css('transition-delay', '0.08s, 0s, 0s')
                    expect(card).to_have_css('transition-duration', '0.16s, 0.16s, 0.16s')
                    assert card.evaluate('el => {const r=el.getBoundingClientRect(); return r.left >= 0 && r.right <= innerWidth+1 && r.bottom <= innerHeight+1 && el.scrollWidth <= el.clientWidth+1;}')
                    page.screenshot(path=str(artifacts / f'{engine}-{width}-observable-main-card.png'))
                    page.keyboard.press('Escape')
                    assert trigger.evaluate('el => el === document.activeElement')
                    page.emulate_media(reduced_motion='reduce', color_scheme='dark')
                    page.locator('html').evaluate("el => el.dataset.theme = 'dark'")
                    trigger.click()
                    expect(page.locator('.uml-card:popover-open')).to_have_css('transition-duration', '0s')
                    expect(page.locator('.uml-card:popover-open[data-positioned]')).to_have_css('opacity', '1')
                    page.screenshot(path=str(artifacts / f'{engine}-{width}-observable-main-dark.png'))
                    page.keyboard.press('Escape')
                    page.emulate_media(reduced_motion='no-preference', color_scheme='light')
                    page.locator('html').evaluate("el => el.dataset.theme = 'light'")
                opener = page.locator('[data-open]')
                opener.scroll_into_view_if_needed()
                position = page.evaluate('scrollY')
                opener.click()
                dialog = page.locator('[data-explorer] dialog')
                reading = page.locator('[data-reading]')
                expect(dialog).to_be_visible()
                assert reading.evaluate('el => el === document.activeElement')
                assert dialog.locator('article:visible').count() == 1
                tabs = dialog.get_by_role('tab')
                tabs.first.focus()
                page.keyboard.press('ArrowRight')
                expect(tabs.first).to_have_attribute('aria-selected', 'true')
                assert tabs.nth(1).evaluate('el => el === document.activeElement && el.tabIndex === 0')
                page.keyboard.press('Enter')
                expect(tabs.nth(1)).to_have_attribute('aria-selected', 'true')
                reading.evaluate('el => el.scrollTop = el.scrollHeight')
                page.keyboard.press('Home')
                page.keyboard.press('Space')
                expect(tabs.first).to_have_attribute('aria-selected', 'true')
                assert reading.evaluate('el => el.scrollTop') == 0
                for key in ['Tab', 'Shift+Tab']:
                    for _ in range(12):
                        page.keyboard.press(key)
                        assert dialog.evaluate('el => el.contains(document.activeElement)')
                for category in [0, 1]:
                    tabs.nth(category).click()
                    for trigger in dialog.locator('.uml-trigger:visible').all():
                        trigger.focus()
                        page.keyboard.press('Enter')
                        card = page.locator('.uml-card:popover-open')
                        expect(card).to_have_count(1)
                        expect(card.locator('table')).to_be_visible()
                        expect(card).to_have_css('opacity', '1')
                        page.screenshot(path=str(artifacts / f'{engine}-{width}-card-{category}.png'))
                        assert card.locator('img').evaluate('el => el.complete && el.naturalWidth > 0 && el.getBoundingClientRect().width <= el.naturalWidth + 1')
                        assert card.evaluate('el => {const r=el.getBoundingClientRect(); return r.left >= 0 && r.right <= innerWidth+1 && r.bottom <= innerHeight+1 && el.scrollWidth <= el.clientWidth+1;}')
                        card.locator('.uml-close').focus()
                        page.keyboard.press('Escape')
                        expect(card).to_have_count(0)
                        expect(dialog).to_be_visible()
                        assert trigger.evaluate('el => el === document.activeElement')
                        trigger.click()
                        page.locator('.uml-card:popover-open .uml-close').click()
                        assert trigger.evaluate('el => el === document.activeElement')
                        trigger.click()
                        page.mouse.click(1, 1)  # Native light dismissal; backdrop does not close the dialog.
                        expect(page.locator('.uml-card:popover-open')).to_have_count(0)
                        expect(dialog).to_be_visible()
                assert reading.evaluate('el => el.scrollWidth <= el.clientWidth+1')
                page.screenshot(path=str(artifacts / f'{engine}-{width}-{route.strip("/").replace("/", "-")}.png'))
                page.keyboard.press('Escape')
                expect(dialog).not_to_be_visible()
                assert opener.evaluate('el => el === document.activeElement')
                assert abs(page.evaluate('scrollY') - position) < 2
                opener.click()
                expect(tabs.first).to_have_attribute('aria-selected', 'true')
                page.locator('[data-close]').click()
                # Reset must survive a real reload, without persistence.
                page.reload()
                page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
                page.locator('[data-open]').click()
                expect(page.get_by_role('tab').first).to_have_attribute('aria-selected', 'true')
                page.locator('[data-close]').click()
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1')
            # Complete-program lessons reuse cards without requiring an explorer.
            for slug, rows in [('programme-minimal', [3, 2]), ('premiers-affichages', [4, 4, 4]), ('cpp-09', [7, 6, 7]), ('premiers-calculs', [6, 6])]:
                page.goto(base + f'/notions/{slug}/')
                page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
                expect(page.locator('.uml-trigger')).to_have_count(len(rows))
                expect(page.locator('[data-explorer]')).to_have_count(0)
                if slug == 'premiers-calculs':
                    for table in page.locator('table.observable-values:visible').all():
                        assert table.evaluate('el => el.scrollWidth <= el.clientWidth + 1')
                for diagram in page.locator('img[src^="/diagrams/"]:visible').all():
                    assert diagram.evaluate('''el => {
                      const r = el.getBoundingClientRect(); const p = el.parentElement;
                      const paper = p.getBoundingClientRect(); const content = p.parentElement.getBoundingClientRect();
                      return el.complete && el.naturalWidth > 0 && r.width <= el.naturalWidth + 1
                        && Math.abs(paper.width - content.width) < 2
                        && Math.abs((r.left + r.right) / 2 - (paper.left + paper.right) / 2) < 2
                        && getComputedStyle(p).backgroundColor === 'rgb(255, 255, 255)';
                    }''')
                    if slug == 'premiers-affichages':
                        diagram_measurements.append(diagram.evaluate('''el => ({
                          viewport: innerWidth, source: el.getAttribute('src'), naturalWidth: el.naturalWidth,
                          renderedWidth: el.getBoundingClientRect().width,
                          paperWidth: el.parentElement.getBoundingClientRect().width,
                          bodyFontSize: getComputedStyle(el.closest('.sl-markdown-content')).fontSize
                        })'''))
                page.locator('img[src^="/diagrams/"]:visible').first.scroll_into_view_if_needed()
                page.screenshot(path=str(artifacts / f'{engine}-{width}-{slug}.png'))
                for index, key in enumerate(['Enter', 'Space', 'Enter'][:len(rows)]):
                    trigger = page.locator('.uml-trigger').nth(index)
                    trigger.focus()
                    trigger.press(key)
                    card = page.locator('.uml-card:popover-open')
                    expect(card).to_have_count(1)
                    expect(card).to_have_css('opacity', '1')
                    expect(card.locator('table')).to_be_visible()
                    assert card.locator('tr').count() == rows[index]
                    if slug == 'premiers-affichages':
                        expected_key = ['ordered', 'reversed', 'joined'][index]
                        expect(card.locator('img')).to_have_attribute('src', f'/diagrams/examples/program-{expected_key}.svg')
                        expect(card).to_have_css('transition-delay', '0.08s, 0s, 0s')
                        expect(card).to_have_css('transition-duration', '0.16s, 0.16s, 0.16s')
                    if slug == 'premiers-calculs':
                        expected_key = ['arithmetic-update', 'literal-replacement'][index]
                        assert page.locator(f'[data-uml="program-{expected_key}"] .uml-card:popover-open').count() == 1
                        assert trigger.evaluate('el => el.popoverTargetElement === el.parentElement.querySelector(".uml-card:popover-open")')
                        expect(card.locator('img')).to_have_attribute('src', f'/diagrams/examples/program-{expected_key}.svg')
                        assert card.locator('img').evaluate('el => el.complete && el.getBoundingClientRect().width <= el.naturalWidth + 1')
                        assert card.locator('table').evaluate('el => el.scrollWidth <= el.clientWidth + 1')
                        expect(card).to_have_css('transition-delay', '0.08s, 0s, 0s')
                        expect(card).to_have_css('transition-duration', '0.16s, 0.16s, 0.16s')
                    if slug == 'cpp-09':
                        expected_key = ['constant-valid', 'constant-rejected', 'constant-wrong'][index]
                        assert trigger.evaluate('el => el.popoverTargetElement === el.parentElement.querySelector(".uml-card:popover-open")')
                        assert page.locator(f'[data-uml="{expected_key}"] .uml-card:popover-open').count() == 1
                        asset = 'constant-wrong-limit' if index == 2 else 'constant-limit'
                        expect(card.locator('img')).to_have_attribute('src', f'/diagrams/examples/{asset}.svg')
                        expect(card).to_have_css('transition-delay', '0.08s, 0s, 0s')
                        expect(card).to_have_css('transition-duration', '0.16s, 0.16s, 0.16s')
                        assert card.locator('table').evaluate('el => el.scrollWidth <= el.clientWidth + 1')
                    assert card.evaluate('el => {const r=el.getBoundingClientRect(); return r.left >= 0 && r.right <= innerWidth+1 && r.bottom <= innerHeight+1 && el.scrollWidth <= el.clientWidth+1;}')
                    page.screenshot(path=str(artifacts / f'{engine}-{width}-{slug}-card-{index}.png'))
                    card.locator('.uml-close').press('Escape')
                    expect(page.locator('.uml-card:popover-open')).to_have_count(0)
                    assert trigger.evaluate('el => el === document.activeElement')
                    trigger.click()
                    page.locator('.uml-card:popover-open .uml-close').click()
                    assert trigger.evaluate('el => el === document.activeElement')
                    trigger.click()
                    page.mouse.click(1, 1)
                    expect(page.locator('.uml-card:popover-open')).to_have_count(0)
                page.locator('.uml-trigger').first.focus()
                page.keyboard.press('Enter')
                page.locator('.uml-trigger').last.focus()
                page.keyboard.press('Enter')
                expect(page.locator('.uml-card:popover-open')).to_have_count(1)
                page.keyboard.press('Escape')
                page.emulate_media(reduced_motion='reduce', color_scheme='dark')
                page.locator('html').evaluate("el => el.dataset.theme = 'dark'")
                page.locator('.uml-trigger').first.click()
                card = page.locator('.uml-card:popover-open[data-positioned]')
                expect(card).to_have_css('opacity', '1')
                expect(card).to_have_css('transition-duration', '0s')
                page.screenshot(path=str(artifacts / f'{engine}-{width}-{slug}-dark.png'))
                page.keyboard.press('Escape')
                if slug == 'premiers-calculs':
                    page.locator('.uml-trigger').last.click()
                    card = page.locator('.uml-card:popover-open[data-positioned]')
                    expect(card).to_have_css('opacity', '1')
                    expect(card).to_have_css('transition-duration', '0s')
                    assert card.locator('tr').count() == 6
                    assert card.locator('table').evaluate('el => el.scrollWidth <= el.clientWidth + 1')
                    page.keyboard.press('Escape')
                page.reload()
                page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
                expect(page.locator('.uml-trigger')).to_have_count(len(rows))
                expect(page.locator('.uml-card:popover-open')).to_have_count(0)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1')
                page.emulate_media(reduced_motion='no-preference', color_scheme='light')
            # Plain Markdown uses the same enhancement as MDX and rendered sheets.
            page.goto(base + '/notions/cpp-09/')
            page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
            for table in page.locator('table.observable-values:visible').all():
                assert table.evaluate('el => el.scrollWidth <= el.clientWidth + 1')
            for index in range(3):
                trigger = page.locator('.uml-trigger').nth(index)
                trigger.focus()
                trigger.press('Enter')
                expect(page.locator('.uml-card:popover-open')).to_have_count(1)
            trigger = page.locator('.uml-trigger').last
            expect(trigger).to_have_text('UML · écart')
            page.keyboard.press('Escape')
            assert trigger.evaluate('el => el === document.activeElement')
            page.emulate_media(reduced_motion='reduce', color_scheme='dark')
            page.locator('html').evaluate("el => el.dataset.theme = 'dark'")
            trigger.click()
            expect(page.locator('.uml-card:popover-open')).to_have_css('transition-duration', '0s')
            page.screenshot(path=str(artifacts / f'{engine}-{width}-const-dark.png'))
            page.close()
        # Text enlargement is a reflow probe, distinct from native browser page zoom.
        page = browser.new_page(viewport={'width': 720, 'height': 900})
        page.goto(base + '/notions/cpp-01/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        page.locator('html').evaluate("el => el.style.fontSize = '200%'")
        page.locator('[data-open]').click()
        assert page.locator('[data-reading]').evaluate('el => el.scrollWidth <= el.clientWidth+1')
        expect(page.locator('[data-close]')).to_be_in_viewport()
        page.screenshot(path=str(artifacts / f'{engine}-text-200-percent.png'))
        for slug in ['cpp-01', 'programme-minimal', 'premiers-affichages', 'cpp-09', 'premiers-calculs']:
            page.goto(base + f'/notions/{slug}/')
            page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
            page.locator('html').evaluate("el => el.style.fontSize = '200%'")
            for table in page.locator('table.observable-values:visible').all():
                assert table.evaluate('el => el.scrollWidth <= el.clientWidth + 1')
            page.locator('.uml-trigger').first.click()
            card = page.locator('.uml-card:popover-open')
            expect(card).to_have_css('opacity', '1')
            assert card.evaluate('el => el.scrollWidth <= el.clientWidth+1')
            expect(card.locator('.uml-close')).to_be_in_viewport()
            for table in card.locator('table.observable-values').all():
                assert table.evaluate('el => el.scrollWidth <= el.clientWidth + 1')
            page.screenshot(path=str(artifacts / f'{engine}-{slug}-text-200-percent.png'))
            if slug == 'premiers-calculs':
                page.keyboard.press('Escape')
                page.locator('.uml-trigger').last.click()
                card = page.locator('.uml-card:popover-open')
                expect(card).to_have_css('opacity', '1')
                assert card.evaluate('el => el.scrollWidth <= el.clientWidth+1')
                assert card.locator('table').evaluate('el => el.scrollWidth <= el.clientWidth+1')
                expect(card.locator('.uml-close')).to_be_in_viewport()

        page.close()
        # Await Pagefind initialization before navigating away: Firefox reports an aborted
        # idle module import if a test leaves a freshly loaded route too quickly.
        # Exercise the published path, the production search index and original SVG links.
        page = browser.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
        page.on('response', lambda response: errors.append(f'HTTP {response.status}: {response.url}') if response.status >= 400 else None)
        page.goto(base + '/notions/programme-minimal/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        page.locator('.pagination-links a[rel="next"]').click()
        expect(page).to_have_url(base + '/notions/premiers-affichages/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        expect(page.locator('.pagination-links a[rel="prev"]')).to_have_attribute('href', '/notions/programme-minimal/')
        page.locator('.pagination-links a[rel="next"]').click()
        expect(page).to_have_url(base + '/notions/cpp-01/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        page.locator('.pagination-links a[rel="next"]').click()
        expect(page).to_have_url(base + '/notions/cpp-09/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        expect(page.locator('.pagination-links a[rel="prev"]')).to_have_attribute('href', '/notions/cpp-01/')
        page.locator('.pagination-links a[rel="next"]').click()
        expect(page).to_have_url(base + '/notions/premiers-calculs/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        expect(page.locator('.pagination-links a[rel="prev"]')).to_have_attribute('href', '/notions/cpp-09/')

        page.get_by_role('button', name='Rechercher', exact=True).click()
        search = page.get_by_role('dialog', name='Rechercher', exact=True)
        search.get_by_placeholder('Rechercher', exact=True).fill('Suivre plusieurs affichages')
        search.locator('a.pagefind-ui__result-link[href="/notions/premiers-affichages/"]').click()
        expect(page).to_have_url(base + '/notions/premiers-affichages/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        for key in ['ordered', 'reversed', 'joined']:
            with page.expect_popup() as opened:
                page.locator(f'a[href="/diagrams/examples/program-{key}.svg"]').first.click()
            original = opened.value
            original.wait_for_load_state()
            assert original.url == base + f'/diagrams/examples/program-{key}.svg'
            expect(original.locator('svg')).to_be_visible()
            original.close()
        page.goto(base + '/notions/cpp-09/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        for asset in ['constant-limit', 'constant-wrong-limit']:
            with page.expect_popup() as opened:
                page.locator(f'a[href="/diagrams/examples/{asset}.svg"]').first.click()
            original = opened.value
            original.wait_for_load_state()
            assert original.url == base + f'/diagrams/examples/{asset}.svg'
            expect(original.locator('svg')).to_be_visible()
            original.close()
        page.get_by_role('button', name='Rechercher', exact=True).click()
        search = page.get_by_role('dialog', name='Rechercher', exact=True)
        search.get_by_placeholder('Rechercher', exact=True).fill('Calculer une nouvelle valeur')
        search.locator('a.pagefind-ui__result-link[href="/notions/premiers-calculs/"]').click()
        expect(page).to_have_url(base + '/notions/premiers-calculs/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        for key in ['arithmetic-update', 'literal-replacement']:
            with page.expect_popup() as opened:
                page.locator(f'a[href="/diagrams/examples/program-{key}.svg"]').first.click()
            original = opened.value
            original.wait_for_load_state()
            assert original.url == base + f'/diagrams/examples/program-{key}.svg'
            expect(original.locator('svg')).to_be_visible()
            original.close()
        page.close()
        # A fixture extends the real generated DOM, keeping teaching additions unpublished.
        page = browser.new_page()
        page.goto(base + '/notions/cpp-01/')
        page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
        page.evaluate('''() => {
          const original = document.querySelector('[data-explorer]');
          const fixture = original.cloneNode(true);
          fixture.removeAttribute('data-ready');
          const fallback = fixture.querySelector('[data-fallback]');
          fallback.hidden = false;
          fixture.querySelectorAll('[data-panel]').forEach(panel => fallback.append(panel));
          fixture.querySelectorAll('[id]').forEach(el => el.id += '-fixture');
          fixture.querySelectorAll('[aria-controls], [aria-labelledby]').forEach(el => {
            for (const attr of ['aria-controls', 'aria-labelledby']) {
              if (el.hasAttribute(attr)) el.setAttribute(attr, el.getAttribute(attr) + '-fixture');
            }
          });
          const panel = fallback.querySelector('[data-panel]');
          const first = panel.querySelector('article');
          const extra = document.createElement('article');
          extra.dataset.example = 'fixture-second';
          extra.innerHTML = '<h3>Second fixture sheet</h3><p>Selection fixture.</p>';
          panel.append(extra);
          const label = document.createElement('label');
          label.className = 'example-selector';
          label.append('Fixture selection');
          const select = document.createElement('select');
          select.append(new Option('First', first.dataset.example), new Option('Second', 'fixture-second'));
          label.append(select);
          panel.prepend(label);
          document.querySelector('main').append(fixture);
          document.dispatchEvent(new Event('astro:page-load'));
        }''')
        fixture = page.locator('[data-explorer]').nth(1)
        fixture.locator('[data-open]').click()
        select = fixture.locator('select')
        select.focus()
        select.select_option('fixture-second')
        assert select.evaluate('el => el === document.activeElement')
        expect(fixture.locator('article:visible h3')).to_have_text('Second fixture sheet')
        fixture.locator('[data-close]').click()
        fixture.locator('[data-open]').click()
        expect(select).to_have_value('component-stock')
        fixture.locator('[data-close]').click()
        page.locator('[data-explorer]').first.locator('[data-open]').click()
        assert page.locator('[data-explorer]').first.locator('article:visible').count() == 1
        page.close()
        # No JavaScript and unsupported popover API both retain native disclosures.
        for javascript in [False, True]:
            context = browser.new_context(java_script_enabled=javascript)
            if javascript:
                context.add_init_script('delete HTMLElement.prototype.showPopover')
            page = context.new_page()
            page.goto(base + '/notions/cpp-01/')
            if javascript:
                page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
                page.locator('[data-open]').click()
                panel = page.locator('dialog details.uml-panel:visible').first
            else:
                assert page.locator('[data-fallback] article:visible').count() == 2
                expect(page.locator('[data-open]')).not_to_be_visible()
                panel = page.locator('details.uml-panel').first
            panel.locator('summary').click()
            expect(panel.locator('table')).to_be_visible()
            expect(panel.locator('img')).to_be_visible()
            if javascript:
                page.locator('[data-close]').click()
            primary = page.locator('details[data-uml="measurement-primary"]')
            if not primary.evaluate('el => el.open'):
                primary.locator('summary').click()
            expect(primary.locator('table')).to_be_visible()
            assert primary.locator('tr').count() == 6
            assert primary.locator('table').evaluate('el => el.scrollWidth <= el.clientWidth + 1')
            for slug, count in [('programme-minimal', 2), ('premiers-affichages', 3), ('cpp-09', 3), ('premiers-calculs', 2)]:
                page.goto(base + f'/notions/{slug}/')
                if javascript:
                    page.locator('#starlight__search .pagefind-ui').wait_for(state='attached')
                expect(page.locator('.uml-trigger')).to_have_count(0)
                for panel in page.locator('details.uml-panel').all():
                    panel.locator('summary').click()
                    expect(panel.locator('table')).to_be_visible()
                    expect(panel.locator('img')).to_be_visible()
                expect(page.locator('details.uml-panel')).to_have_count(count)
            context.close()
        browser.close()
    assert not errors, errors
    (artifacts / f'{engine}-result.json').write_text(json.dumps({
        'engine': engine, 'errors': errors, 'status': 'passed', 'diagrams': diagram_measurements,
    }, indent=2))
    print(f'PASS {engine}: dialog, cards, keyboard, focus, mobile, theme, fixtures, reload and fallbacks')
finally:
    server.shutdown()
