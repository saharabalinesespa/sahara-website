/* Sahara analytics — Google tag (GA4) + GTM data layer. Skips local testing. */
(function () {
  'use strict';
  var h = location.hostname; if (h === 'localhost' || h === '127.0.0.1' || h === '') { window.sahTrack = function () {}; return; }
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  gtag('js', new Date());
  gtag('config', 'G-HD07N96RGX');
  /* sahTrack(name, params): one call -> GA4 event + GTM dataLayer event (use either in GTM, not both, to avoid double counting) */
  window.sahTrack = function (name, params) {
    params = params || {};
    try { gtag('event', name, params); var o = { event: name }; for (var k in params) o[k] = params[k]; window.dataLayer.push(o); } catch (e) {}
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a'); if (!a) return;
    var href = a.getAttribute('href') || '', t = a.getAttribute('data-track');
    if (t) return window.sahTrack(t, { link_url: href, page: location.pathname });
    if (href.indexOf('wa.me') > -1 || href.indexOf('whatsapp') > -1) window.sahTrack('whatsapp_click', { link_url: href, page: location.pathname });
    else if (href.indexOf('tel:') === 0) window.sahTrack('phone_click', { phone: href.slice(4), page: location.pathname });
    else if (href.indexOf('mailto:') === 0) window.sahTrack('email_click', { page: location.pathname });
    else if (href.indexOf('book.html') > -1) window.sahTrack('book_click', { page: location.pathname });
  }, true);
  /* WhatsApp-request forms (used when online booking is off): count them as leads */
  document.addEventListener('submit', function (e) {
    var id = e.target && e.target.id; if (id === 'bk-form' || id === 'v-form' || id === 'c-form') window.sahTrack('generate_lead', { form: id, page: location.pathname });
  });
})();
