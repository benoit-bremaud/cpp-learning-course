/** Enhance authored disclosures while preserving their no-script reading fallback. */
export function initializeUmlCards(): void {
  if (!('showPopover' in HTMLElement.prototype)) return;
  document.querySelectorAll<HTMLDetailsElement>('details.uml-panel:not([data-card-ready])').forEach(panel => {
    const summary = panel.querySelector('summary');
    if (!summary) return;
    const label = summary.textContent?.trim() || 'Voir la conception UML';
    const trigger = document.createElement('button');
    trigger.type = 'button';
    trigger.className = 'uml-trigger';
    trigger.textContent = label.includes('écart') ? 'UML · écart' : 'UML';
    trigger.setAttribute('aria-label', label);
    const card = document.createElement('div');
    card.id = `uml-${crypto.randomUUID()}`;
    card.className = 'uml-card';
    card.popover = 'auto';
    card.setAttribute('role', 'region');
    card.setAttribute('aria-label', label);
    trigger.popoverTargetElement = card;
    const close = document.createElement('button');
    close.type = 'button';
    close.className = 'uml-close';
    close.textContent = 'Fermer';
    close.setAttribute('aria-label', 'Fermer la carte UML');
    close.addEventListener('click', () => {
      card.hidePopover();
      trigger.focus({ preventScroll: true });
    });
    card.append(close);
    [...panel.childNodes].filter(node => node !== summary).forEach(node => card.append(node));
    summary.hidden = true;
    panel.open = true;
    panel.dataset.cardReady = 'true';
    panel.append(trigger, card);
    const position = (): void => {
      const anchor = trigger.getBoundingClientRect();
      const gap = 8;
      const height = card.getBoundingClientRect().height;
      const left = Math.max(gap, Math.min(anchor.right - card.offsetWidth, innerWidth - card.offsetWidth - gap));
      const top = Math.max(gap, Math.min(anchor.bottom + gap, innerHeight - height - gap));
      card.style.left = `${left}px`;
      card.style.top = `${top}px`;
    };
    // Keep the first paint hidden until the final viewport position is known.
    card.addEventListener('beforetoggle', event => {
      if ((event as ToggleEvent).newState === 'open') delete card.dataset.positioned;
    });
    card.addEventListener('toggle', () => {
      if (card.matches(':popover-open')) {
        card.scrollTop = 0;
        position();
        card.dataset.positioned = 'true';
        window.addEventListener('resize', position);
      } else window.removeEventListener('resize', position);
    });
    // Handle Escape before the surrounding example dialog can consume it.
    panel.addEventListener('keydown', event => {
      if (event.key === 'Escape' && card.matches(':popover-open')) {
        event.preventDefault();
        event.stopPropagation();
        card.hidePopover();
        trigger.focus({ preventScroll: true });
      }
    });
    const dialog = panel.closest('dialog');
    dialog?.addEventListener('close', () => card.hidePopover());
  });
}
