"""Local browser acceptance checks. Requires Python Playwright and Google Chrome.
Run after npm test: python3 tests/explorer-browser.py
Serves dist on a temporary loopback port; no deployment or external service.
"""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright, expect

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass

server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(Path("dist").resolve())))
Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        for width, height in [(1440, 1000), (390, 844), (320, 640)]:
            page = browser.new_page(viewport={"width": width, "height": height})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            for route in ["/notions/cpp-01/", "/exemple-voyant/", "/notions/premieres-expressions/"]:
                page.goto(base + route)
                opener = page.locator("[data-open]")
                opener.scroll_into_view_if_needed()
                position = page.evaluate("window.scrollY")
                opener.click()
                dialog = page.locator("[data-explorer] dialog")
                assert dialog.is_visible()
                assert page.locator("[data-reading]").evaluate("el => el === document.activeElement")
                assert page.locator("[data-explorer] dialog article:visible").count() == 1
                assert page.locator("[data-explorer] dialog select").count() == 0
                tabs = dialog.get_by_role("tab")
                tabs.nth(0).focus()
                page.keyboard.press("ArrowRight")
                assert tabs.nth(0).get_attribute("aria-selected") == "true"
                page.keyboard.press("Enter")
                assert tabs.nth(1).get_attribute("aria-selected") == "true"
                assert page.locator("[data-explorer] dialog article:visible").count() == 1
                page.locator("[data-reading]").evaluate("el => el.scrollTop = el.scrollHeight")
                tabs.nth(0).click()
                assert page.locator("[data-reading]").evaluate("el => el.scrollTop") == 0
                for _ in range(12):
                    page.keyboard.press("Tab")
                    assert dialog.evaluate("el => el.contains(document.activeElement)")
                for _ in range(12):
                    page.keyboard.press("Shift+Tab")
                    assert dialog.evaluate("el => el.contains(document.activeElement)")
                assert page.locator("[data-reading]").evaluate("el => el.scrollWidth <= el.clientWidth + 1")
                page.screenshot(path=f"/tmp/example-explorer-{width}-{route.strip('/').replace('/', '-')}.png")
                page.keyboard.press("Escape")
                assert not dialog.is_visible()
                assert opener.evaluate("el => el === document.activeElement")
                assert abs(page.evaluate("window.scrollY") - position) < 2
                opener.click()
                assert tabs.nth(0).get_attribute("aria-selected") == "true"
                page.locator("[data-close]").click()
                assert not dialog.is_visible()
            assert not errors, errors
            page.close()
        # Compact cards work in both loaders and inside the existing modal.
        for width in [1440, 390, 320]:
            page = browser.new_page(viewport={"width": width, "height": 900})
            for route, count in [("/notions/cpp-01/", 6), ("/notions/premieres-expressions/", 5), ("/notions/premieres-soustractions/", 4), ("/notions/premieres-multiplications/", 5), ("/notions/parentheses-calculs/", 5), ("/notions/premieres-divisions/", 4), ("/notions/mise-a-jour-compteur/", 6), ("/notions/premiers-booleens/", 6), ("/notions/premiere-comparaison/", 5), ("/notions/atteindre-ou-depasser/", 5), ("/notions/en-dessous-ou-au-maximum/", 5), ("/notions/egal-ou-different/", 5), ("/notions/premiere-condition/", 4), ("/notions/cpp-09/", 3), ("/exemple-voyant/", 4), ("/notions/programme-minimal/", 2), ("/notions/premiers-affichages/", 3)]:
                page.goto(base + route)
                assert page.locator(".uml-trigger").count() == count
                assert page.locator("details.uml-panel > summary:visible").count() == 0
                groups = [None]
                if page.locator("[data-open]").count():
                    groups += [0, 1]
                for group in groups:
                    if group is not None:
                        page.locator("[data-open]").click()
                        page.get_by_role("tab").nth(group).click()
                        scope = page.locator("[data-explorer] dialog")
                    else:
                        scope = page.locator("main")
                    for trigger in scope.locator(".uml-trigger:visible").all():
                        trigger.focus()
                        page.keyboard.press("Enter")
                        card = page.locator(".uml-card:popover-open")
                        assert card.count() == 1
                        expect(card.locator("table")).to_be_visible()
                        assert card.locator("img").evaluate("el => el.complete && el.naturalWidth > 0")
                        assert card.evaluate("el => { const r = el.getBoundingClientRect(); return r.left >= 0 && r.right <= innerWidth && r.bottom <= innerHeight && el.scrollWidth <= el.clientWidth + 1; }")
                        page.screenshot(path=f"/tmp/uml-card-{width}-{group}.png")
                        card.locator(".uml-close").focus()
                        page.keyboard.press("Escape")
                        assert page.locator(".uml-card:popover-open").count() == 0
                        assert trigger.evaluate("el => el === document.activeElement")
                        if group is not None:
                            assert page.locator("[data-explorer] dialog").is_visible()
                        trigger.click()
                        card.locator(".uml-close").click()
                        assert trigger.evaluate("el => el === document.activeElement")
                        trigger.click()
                        if group is not None:
                            page.locator(".explorer-header h2").click()
                            assert page.locator("[data-explorer] dialog").is_visible()
                        else:
                            page.mouse.click(2, 2)
                        assert page.locator(".uml-card:popover-open").count() == 0
                    if group is not None:
                        page.locator("[data-close]").click()
            page.close()
        page = browser.new_page()
        page.goto(base + "/notions/cpp-09/")
        triggers = page.locator(".uml-trigger")
        triggers.nth(0).click()
        triggers.nth(1).evaluate("el => el.click()")
        assert page.locator(".uml-card:popover-open").count() == 1
        assert triggers.nth(1).evaluate("el => el.popoverTargetElement.matches(':popover-open')")
        card = page.locator(".uml-card:popover-open")
        with page.expect_popup() as opened:
            card.get_by_role("link", name="Ouvrir le diagramme en grand — nouvel onglet").click()
        popup = opened.value
        popup.wait_for_load_state()
        assert popup.url.endswith("/diagrams/examples/constant-limit.svg")
        popup.close()
        page.close()
        # Opening must fade at a stable position, including repeated openings.
        for width in [1440, 320]:
            page = browser.new_page(viewport={"width": width, "height": 900})
            page.goto(base + "/notions/cpp-09/")
            trigger = page.locator(".uml-trigger").first
            trigger.scroll_into_view_if_needed()
            for _ in range(2):
                samples = trigger.evaluate("""async button => {
                  const card = button.popoverTargetElement;
                  const samples = [];
                  button.click();
                  const start = performance.now();
                  while (performance.now() - start < 350) {
                    await new Promise(requestAnimationFrame);
                    const style = getComputedStyle(card);
                    const rect = card.getBoundingClientRect();
                    samples.push({opacity: Number(style.opacity), visibility: style.visibility,
                      x: rect.x, y: rect.y, positioned: !!card.dataset.positioned});
                  }
                  return samples;
                }""")
                visible = [s for s in samples if s["visibility"] == "visible" and s["opacity"] > 0]
                assert visible and all(s["positioned"] for s in visible)
                assert max(s["y"] for s in visible) - min(s["y"] for s in visible) < 1
                assert max(s["x"] for s in visible) - min(s["x"] for s in visible) < 1
                assert samples[-1]["opacity"] == 1
                closing = trigger.evaluate("""async button => {
                  const card = button.popoverTargetElement;
                  const samples = [];
                  card.querySelector('.uml-close').click();
                  const start = performance.now();
                  while (performance.now() - start < 250) {
                    await new Promise(requestAnimationFrame);
                    const style = getComputedStyle(card);
                    samples.push({opacity: Number(style.opacity), display: style.display});
                  }
                  return samples;
                }""")
                assert any(0 < s["opacity"] < 1 and s["display"] != "none" for s in closing)
                assert closing[-1]["display"] == "none"
                assert trigger.evaluate("el => el === document.activeElement")
            page.emulate_media(reduced_motion="reduce")
            trigger.click()
            assert page.locator(".uml-card:popover-open").evaluate("el => getComputedStyle(el).transitionDuration") == "0s"
            page.close()
        # Multiple-sheet and multiple-instance fixture uses real generated markup and the real script.
        page = browser.new_page()
        page.goto(base + "/notions/cpp-01/")
        page.evaluate("""() => {
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
          const extra = first.cloneNode(true);
          extra.dataset.example = 'fixture-second';
          extra.querySelector('h3').textContent = 'Second test example';
          extra.querySelectorAll('[id]').forEach(el => el.id += '-second');
          panel.append(extra);
          const select = document.createElement('select');
          select.append(new Option('First', first.dataset.example), new Option('Second', 'fixture-second'));
          panel.prepend(select);
          document.querySelector('main').append(fixture);
          document.dispatchEvent(new Event('astro:page-load'));
        }""")
        fixture = page.locator('[data-explorer]').nth(1)
        fixture.locator('[data-open]').click()
        fixture.locator('select').select_option('fixture-second')
        assert fixture.locator('article:visible').count() == 1
        assert fixture.locator('article:visible h3').first.inner_text() == 'Second test example'
        fixture.locator('[data-close]').click()
        page.locator('[data-explorer]').first.locator('[data-open]').click()
        assert page.locator('[data-explorer]').first.locator('article:visible').count() == 1
        page.close()
        context = browser.new_context(java_script_enabled=False)
        page = context.new_page()
        page.goto(base + '/notions/cpp-01/')
        assert page.locator('[data-fallback] article:visible').count() == 2
        assert not page.locator('[data-open]').is_visible()
        panel = page.locator("details.uml-panel").first
        panel.locator("summary").click()
        assert panel.locator("table").is_visible()
        for route, count in [('/notions/mise-a-jour-compteur/', 6), ('/notions/premiers-booleens/', 6), ('/notions/premiere-comparaison/', 5), ('/notions/atteindre-ou-depasser/', 5), ('/notions/en-dessous-ou-au-maximum/', 5), ('/notions/egal-ou-different/', 5), ('/notions/premiere-condition/', 4)]:
            page.goto(base + route)
            assert page.locator('details.uml-panel').count() == count
            for panel in page.locator('details.uml-panel').all():
                panel.locator('summary').click()
                expect(panel.locator('table')).to_be_visible()
                expect(panel.locator('img')).to_be_visible()
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(base + '/notions/mise-a-jour-compteur/')
        trigger = page.locator('[data-uml="counter-reset"] .uml-trigger')
        expect(trigger).to_have_text('UML · écart')
        trigger.click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Attendu : 0 → 1 → 2 ; obtenu : 0 → 1 → 1.')
        expect(card).to_have_css('opacity', '1')
        page.screenshot(path='/tmp/counter-update-mobile.png')
        page.goto(base + '/notions/premiers-booleens/')
        trigger = page.locator('[data-uml="boolean-wrong"] .uml-trigger')
        expect(trigger).to_have_text('UML · écart')
        trigger.click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Attendu : false ; obtenu : true.')
        expect(card).to_have_css('opacity', '1')
        page.screenshot(path='/tmp/boolean-values-mobile.png')
        page.goto(base + '/notions/premiere-comparaison/')
        trigger = page.locator('[data-uml="comparison-reversed"] .uml-trigger')
        expect(trigger).to_have_text('UML · écart')
        trigger.click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Attendu : true ; obtenu : false.')
        expect(card).to_have_css('opacity', '1')
        page.screenshot(path='/tmp/first-comparison-mobile.png')
        card.locator('.uml-close').click()
        page.locator('[data-uml="comparison-refresh"] .uml-trigger').click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_have_css('opacity', '1')
        card.evaluate('el => el.scrollTop = el.scrollHeight')
        page.screenshot(path='/tmp/first-comparison-refresh-mobile.png')
        page.goto(base + '/notions/atteindre-ou-depasser/')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
        for key, result in [('strict-for-inclusive', 'false / false'), ('inclusive-for-strict', 'true / true')]:
            trigger = page.locator(f'[data-uml="inclusive-{key}"] .uml-trigger')
            expect(trigger).to_have_text('UML · écart')
            trigger.click()
            card = page.locator('.uml-card:popover-open')
            expect(card).to_contain_text(f'Attendu : false / true ; obtenu : {result}.')
            expect(card).to_have_css('opacity', '1')
            page.screenshot(path=f'/tmp/inclusive-{key}-mobile.png')
            card.locator('.uml-close').click()
        page.locator('[data-uml="inclusive-equal"] .uml-trigger').click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_have_css('opacity', '1')
        card.evaluate('el => el.scrollTop = el.scrollHeight')
        page.screenshot(path='/tmp/inclusive-equal-mobile.png')
        page.goto(base + '/notions/en-dessous-ou-au-maximum/')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
        trigger = page.locator('[data-uml="lower-reversed"] .uml-trigger')
        expect(trigger).to_have_text('UML · écart')
        trigger.click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Attendu : true / true ; obtenu : false / true.')
        expect(card).to_have_css('opacity', '1')
        page.screenshot(path='/tmp/lower-reversed-mobile.png')
        card.locator('.uml-close').click()
        page.locator('[data-uml="lower-capacity"] .uml-trigger').click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('has_space')
        expect(card).to_contain_text('within_capacity')
        expect(card).to_have_css('opacity', '1')
        card.evaluate('el => el.scrollTop = el.scrollHeight')
        page.screenshot(path='/tmp/lower-capacity-mobile.png')
        page.goto(base + '/notions/egal-ou-different/')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
        trigger = page.locator('[data-uml="equality-threshold"] .uml-trigger')
        expect(trigger).to_have_text('UML · écart')
        trigger.click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Attendu : false / true ; obtenu : true / true.')
        expect(card).to_have_css('opacity', '1')
        page.screenshot(path='/tmp/equality-threshold-mobile.png')
        card.locator('.uml-close').click()
        page.locator('[data-uml="equality-identifier"] .uml-trigger').click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('identifier_matched')
        expect(card).to_contain_text('identifier_different')
        expect(card).to_have_css('opacity', '1')
        card.evaluate('el => el.scrollTop = el.scrollHeight')
        page.screenshot(path='/tmp/equality-identifier-mobile.png')
        page.goto(base + '/notions/premiere-condition/')
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1')
        trigger = page.locator('[data-uml="first-if-misplaced"] .uml-trigger')
        expect(trigger).to_have_text('UML · écart')
        trigger.click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Attendu : Check finished suivi d’un saut de ligne ; obtenu : aucun texte.')
        expect(card).to_have_css('opacity', '1')
        page.screenshot(path='/tmp/first-if-misplaced-mobile.png')
        card.locator('.uml-close').click()
        page.locator('[data-uml="first-if-unmatched"] .uml-trigger').click()
        card = page.locator('.uml-card:popover-open')
        expect(card).to_contain_text('Check finished')
        expect(card).to_have_css('opacity', '1')
        card.evaluate('el => el.scrollTop = el.scrollHeight')
        page.screenshot(path='/tmp/first-if-unmatched-mobile.png')
        browser.close()
    print('PASS: desktop/mobile/narrow reading, tabs, focus, closing, scroll, fixtures and no-JS fallback')
finally:
    server.shutdown()
