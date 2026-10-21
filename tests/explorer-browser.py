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
try:
    with sync_playwright() as pw:
        browser = getattr(pw, engine).launch(executable_path=executable)
        for width, height in [(1440, 1000), (390, 844), (320, 640)]:
            page = browser.new_page(viewport={'width': width, 'height': height})
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
            page.on('response', lambda response: errors.append(f'HTTP {response.status}: {response.url}') if response.status >= 400 else None)
            for route in ['/notions/cpp-01/', '/exemple-voyant/']:
                page.goto(base + route)
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
                        assert card.locator('img').evaluate('el => el.complete && el.naturalWidth > 0')
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
                page.locator('[data-open]').click()
                expect(page.get_by_role('tab').first).to_have_attribute('aria-selected', 'true')
                page.locator('[data-close]').click()
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1')
            # Plain Markdown uses the same enhancement as MDX and rendered sheets.
            page.goto(base + '/notions/cpp-09/')
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
        page.locator('html').evaluate("el => el.style.fontSize = '200%'")
        page.locator('[data-open]').click()
        assert page.locator('[data-reading]').evaluate('el => el.scrollWidth <= el.clientWidth+1')
        expect(page.locator('[data-close]')).to_be_in_viewport()
        page.screenshot(path=str(artifacts / f'{engine}-text-200-percent.png'))
        page.close()
        # A fixture extends the real generated DOM, keeping teaching additions unpublished.
        page = browser.new_page()
        page.goto(base + '/notions/cpp-01/')
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
                page.locator('[data-open]').click()
                panel = page.locator('dialog details.uml-panel:visible').first
            else:
                assert page.locator('[data-fallback] article:visible').count() == 2
                expect(page.locator('[data-open]')).not_to_be_visible()
                panel = page.locator('details.uml-panel').first
            panel.locator('summary').click()
            expect(panel.locator('table')).to_be_visible()
            expect(panel.locator('img')).to_be_visible()
            context.close()
        browser.close()
    assert not errors, errors
    (artifacts / f'{engine}-result.json').write_text(json.dumps({'engine': engine, 'errors': errors, 'status': 'passed'}, indent=2))
    print(f'PASS {engine}: dialog, cards, keyboard, focus, mobile, theme, fixtures, reload and fallbacks')
finally:
    server.shutdown()
