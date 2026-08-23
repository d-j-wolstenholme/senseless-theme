/*
 * Senseless — cart add-on offer behaviour (dismiss + quantity stepper + dismissed-state re-apply).
 *
 * Loaded GLOBALLY from layout/theme.liquid (defer), NOT inline in the snippet. The offer markup
 * (snippets/senseless-cart-offer.liquid via cart-summary.liquid) is injected by Horizon when the
 * cart drawer re-renders on add-to-cart — and inline <script> tags inserted as HTML do NOT execute
 * per the HTML spec, so the inline version never ran. This asset runs once on page load and uses
 * document-level delegated listeners + e.target.closest(), which survive every cart re-render.
 *
 * DISMISSAL IS PER-OFFER (23 Aug 2026). The drawer now carries two offers (ointment + cosmetics
 * bag), so the old single global key would have let one dismissal hide both. The key is now
 * 'ss-cart-offer-dismissed:<handle>', read from the card's own data-ss-cart-offer value.
 */
(function () {
  if (window.__ssCartOfferInit) { window.__ssCartOfferApply && window.__ssCartOfferApply(); return; }
  window.__ssCartOfferInit = true;
  var KEY_PREFIX = 'ss-cart-offer-dismissed:';

  function keyFor(el) {
    // Cards always carry their product handle; fall back to a shared key if one ever doesn't,
    // so a card can still be dismissed rather than becoming permanently un-dismissable.
    var handle = el && el.getAttribute('data-ss-cart-offer');
    return KEY_PREFIX + (handle || 'default');
  }

  function isDismissed(el) {
    try { return sessionStorage.getItem(keyFor(el)) === '1'; } catch (e) { return false; }
  }

  function apply() {
    document.querySelectorAll('[data-ss-cart-offer]').forEach(function (el) {
      if (isDismissed(el)) el.setAttribute('hidden', '');
    });
  }
  window.__ssCartOfferApply = apply;

  // Dismiss (delegated — survives cart re-renders). Hides only the card that was dismissed.
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('[data-ss-cart-offer-dismiss]');
    if (!btn) return;
    var row = btn.closest('[data-ss-cart-offer]');
    if (!row) return;
    try { sessionStorage.setItem(keyFor(row), '1'); } catch (e2) {}
    row.setAttribute('hidden', '');
  });

  // Quantity stepper (delegated — survives cart re-renders). Writes to the
  // form's name="quantity" input, which Horizon's add flow reads via FormData.
  // Already per-card via closest(), so it needed no change for the second offer.
  document.addEventListener('click', function (e) {
    if (!e.target.closest) return;
    var dec = e.target.closest('[data-ss-co-dec]');
    var inc = e.target.closest('[data-ss-co-inc]');
    if (!dec && !inc) return;
    var card = (dec || inc).closest('[data-ss-cart-offer]');
    if (!card) return;
    var input = card.querySelector('[data-ss-co-qin]');
    var disp = card.querySelector('[data-ss-co-qval]');
    var n = parseInt(input && input.value, 10) || 1;
    n = inc ? n + 1 : Math.max(1, n - 1);
    if (input) input.value = n;
    if (disp) disp.textContent = n;
  });

  // Re-apply dismissed state whenever the cart drawer/section re-renders.
  var obs = new MutationObserver(function () { apply(); });
  obs.observe(document.documentElement, { childList: true, subtree: true });
  apply();
})();
