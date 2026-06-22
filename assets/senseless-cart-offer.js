/*
 * Senseless — cart add-on offer behaviour (dismiss + quantity stepper + dismissed-state re-apply).
 *
 * Loaded GLOBALLY from layout/theme.liquid (defer), NOT inline in the snippet. The offer markup
 * (snippets/senseless-cart-offer.liquid via cart-summary.liquid) is injected by Horizon when the
 * cart drawer re-renders on add-to-cart — and inline <script> tags inserted as HTML do NOT execute
 * per the HTML spec, so the inline version never ran. This asset runs once on page load and uses
 * document-level delegated listeners + e.target.closest(), which survive every cart re-render.
 */
(function () {
  if (window.__ssCartOfferInit) { window.__ssCartOfferApply && window.__ssCartOfferApply(); return; }
  window.__ssCartOfferInit = true;
  var KEY = 'ss-cart-offer-dismissed';
  function apply() {
    var dismissed = false;
    try { dismissed = sessionStorage.getItem(KEY) === '1'; } catch (e) {}
    if (!dismissed) return;
    document.querySelectorAll('[data-ss-cart-offer]').forEach(function (el) { el.setAttribute('hidden', ''); });
  }
  window.__ssCartOfferApply = apply;
  // Dismiss (delegated — survives cart re-renders).
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('[data-ss-cart-offer-dismiss]');
    if (!btn) return;
    try { sessionStorage.setItem(KEY, '1'); } catch (e2) {}
    var row = btn.closest('[data-ss-cart-offer]');
    if (row) row.setAttribute('hidden', '');
  });
  // Quantity stepper (delegated — survives cart re-renders). Writes to the
  // form's name="quantity" input, which Horizon's add flow reads via FormData.
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
