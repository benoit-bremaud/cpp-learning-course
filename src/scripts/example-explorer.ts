/** Enhance statically rendered sheets without duplicating their content or IDs. */
export function initializeExplorers(): void {
  document.querySelectorAll<HTMLElement>('[data-explorer]').forEach(root => {
    if (root.dataset.ready) return;
    const dialog = root.querySelector('dialog');
    const opener = root.querySelector<HTMLButtonElement>('[data-open]');
    const closer = root.querySelector<HTMLButtonElement>('[data-close]');
    const reading = root.querySelector<HTMLElement>('[data-reading]');
    const fallback = root.querySelector<HTMLElement>('[data-fallback]');
    if (!dialog || !opener || !closer || !reading || !fallback || typeof dialog.showModal !== 'function') return;
    const tabs = [...root.querySelectorAll<HTMLButtonElement>('[role="tab"]')];
    const panels = [...fallback.querySelectorAll<HTMLElement>('[data-panel]')];
    let scrollPosition = 0;
    function selectSheet(panel: HTMLElement, id?: string): void {
      const articles = [...panel.querySelectorAll<HTMLElement>('[data-example]')];
      articles.forEach((article, index) => { article.hidden = id ? article.dataset.example !== id : index !== 0; });
      const select = panel.querySelector<HTMLSelectElement>('select');
      if (select && !id) select.selectedIndex = 0;
      if (reading) reading.scrollTop = 0;
    }
    function activate(index: number): void {
      tabs.forEach((tab, i) => {
        tab.setAttribute('aria-selected', String(i === index));
        tab.tabIndex = i === index ? 0 : -1;
      });
      panels.forEach((panel, i) => { panel.hidden = i !== index; });
      selectSheet(panels[index]);
    }
    panels.forEach((panel, index) => {
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', tabs[index].id);
      const heading = panel.querySelector<HTMLElement>('[data-fallback-heading]');
      if (heading) heading.hidden = true;
      panel.querySelector('select')?.addEventListener('change', event => {
        if (event.target instanceof HTMLSelectElement) selectSheet(panel, event.target.value);
      });
      reading.append(panel);
    });
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => activate(index));
      tab.addEventListener('keydown', event => {
        let next: number;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === 'Home') next = 0;
        else if (event.key === 'End') next = tabs.length - 1;
        else return;
        event.preventDefault();
        tabs[next].focus();
      });
    });
    opener.addEventListener('click', () => {
      scrollPosition = window.scrollY;
      activate(0);
      dialog.showModal();
      reading.focus({ preventScroll: true });
    });
    // Keep sequential keyboard navigation in the modal, including at its edges.
    dialog.addEventListener('keydown', event => {
      if (event.key !== 'Tab') return;
      const controls = [...dialog.querySelectorAll<HTMLElement>('button, a[href], select, input, textarea, summary, [tabindex]')]
        .filter(element => ![...dialog.querySelectorAll('details:not([open])')].some(details =>
          details.contains(element) && element !== details.querySelector('summary')))
        .filter(element => element.tabIndex >= 0 && element.getClientRects().length > 0 && !element.matches(':disabled'));
      const first = controls[0];
      const last = controls[controls.length - 1];
      if (!first || !last) return;
      if (event.shiftKey && (document.activeElement === first || document.activeElement === reading)) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
    closer.addEventListener('click', () => dialog.close());
    dialog.addEventListener('close', () => {
      opener.focus({ preventScroll: true });
      window.scrollTo({ top: scrollPosition, behavior: 'instant' });
    });
    fallback.hidden = true;
    opener.hidden = false;
    root.dataset.ready = 'true';
  });
}
