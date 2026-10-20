"""Focused browser checks for the repeated-decision lesson."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright, expect


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


server = ThreadingHTTPServer(
    ('127.0.0.1', 0),
    partial(QuietHandler, directory=str(Path('dist').resolve())),
)
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'

try:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path='/usr/bin/google-chrome', args=['--no-sandbox']
        )
        for width in [1440, 390, 320]:
            page = browser.new_page(viewport={'width': width, 'height': 900})
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(base + '/notions/repeter-jusqua-limite/')
            assert page.locator('.uml-trigger').count() == 7
            assert page.locator('details.uml-panel > summary:visible').count() == 0
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')

            for key in ['missing-update', 'inclusive-error', 'multiple']:
                trigger = page.locator(f'[data-uml="repeated-{key}"] .uml-trigger')
                trigger.scroll_into_view_if_needed()
                trigger.click()
                card = page.locator('.uml-card:popover-open')
                expect(card).to_be_visible()
                expect(card).to_have_css('opacity', '1')
                assert card.locator('img').evaluate(
                    'element => element.complete && element.naturalWidth > 0'
                )
                assert card.evaluate(
                    'element => { const box = element.getBoundingClientRect(); '
                    'return box.left >= 0 && box.right <= innerWidth '
                    '&& box.bottom <= innerHeight '
                    '&& element.scrollWidth <= element.clientWidth + 1; }'
                )
                if key == 'missing-update':
                    expect(trigger).to_have_text('UML · écart')
                    expect(card).to_contain_text(
                        'Attendu : 1 → 2 → 3 puis sortie ; obtenu : 1 → 1 → 1… sans sortie.'
                    )
                elif key == 'inclusive-error':
                    expect(trigger).to_have_text('UML · écart')
                    expect(card).to_contain_text(
                        'Attendu : sortie à 3 ; obtenu : un passage supplémentaire jusqu’à 4.'
                    )
                else:
                    expect(trigger).to_have_text('UML')
                    card.evaluate('element => element.scrollTop = element.scrollHeight')
                if width == 390:
                    page.screenshot(path=f'/tmp/repeated-{key}-mobile.png')
                card.locator('.uml-close').click()
                assert trigger.evaluate('element => element === document.activeElement')

            assert not errors, errors
            page.close()
        browser.close()
    print('PASS: repeated-decision cards at desktop/mobile/narrow widths, errors, images, focus and overflow')
finally:
    server.shutdown()
