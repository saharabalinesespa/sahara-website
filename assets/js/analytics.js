/* Sahara analytics — Google tag (GA4) + GTM data layer, with Google Consent Mode v2.
   Analytics/ad storage stays DENIED until the visitor accepts in the banner (UAE PDPL). Funnel events: see FUNNEL.md. */
(function () {
  'use strict';
  var KEY = 'sah-consent', GA = 'G-HD07N96RGX';
  var local = /^(localhost|127\.0\.0\.1|)$/.test(location.hostname) && !window.SAH_TEST;
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  var saved = null; try { saved = localStorage.getItem(KEY); } catch (e) {}
  var state = function (v) { return v === 'granted' ? 'granted' : 'denied'; };
  if (!local) {
    gtag('consent', 'default', { analytics_storage: state(saved), ad_storage: state(saved), ad_user_data: state(saved), ad_personalization: state(saved), wait_for_update: 500 });
    gtag('set', 'url_passthrough', true); gtag('set', 'ads_data_redaction', true);
    gtag('js', new Date());
    gtag('config', GA);
  }
  function setConsent(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
    if (!local) { gtag('consent', 'update', { analytics_storage: state(v), ad_storage: state(v), ad_user_data: state(v), ad_personalization: state(v) }); window.dataLayer.push({ event: 'sah_consent_' + v }); }
    var b = document.getElementById('sah-consent'); if (b) b.remove();
  }
  function banner() {
    if (document.getElementById('sah-consent')) return;
    if (!document.getElementById('sah-consent-css')) { var st = document.createElement('style'); st.id = 'sah-consent-css'; st.textContent = '#sah-consent{position:fixed;left:12px;right:12px;bottom:72px;z-index:99999;background:#1e1a12;color:#f5ecd6;border:1px solid #DBA83C;padding:14px 16px;display:flex;gap:14px;align-items:center;justify-content:space-between;flex-wrap:wrap;max-width:760px;margin:0 auto;font:13.5px/1.5 Arial,sans-serif;box-shadow:0 8px 30px rgba(0,0,0,.45)}#sah-consent p{margin:0;flex:1 1 280px}#sah-consent a{color:inherit;text-decoration:underline;display:inline-block;padding:10px 0}#sah-consent button{min-height:44px;min-width:96px;padding:0 18px;border:1px solid #DBA83C;background:none;color:inherit;cursor:pointer;font:inherit}#sah-consent #sah-yes{background:#DBA83C;color:#14110c;font-weight:600}@media(min-width:900px){#sah-consent{bottom:18px}}'; document.head.appendChild(st); }
    var d = document.createElement('div'); d.id = 'sah-consent'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-label', 'Cookie choices');
    d.innerHTML = '<p>We use analytics cookies to see which steps of booking work and where people get stuck. They are off unless you accept. <a href="privacy-policy.html">Privacy Policy</a></p><div><button type="button" id="sah-no">Decline</button><button type="button" id="sah-yes">Accept</button></div>';
    document.body.appendChild(d);
    document.getElementById('sah-yes').onclick = function () { setConsent('granted'); };
    document.getElementById('sah-no').onclick = function () { setConsent('denied'); };
  }
  function ready(fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }
  ready(function () {
    if (!saved) banner();
    document.addEventListener('click', function (e) { var c = e.target.closest && e.target.closest('[data-cookie-settings]'); if (c) { e.preventDefault(); banner(); } });
    /* page-level funnel stages */
    var mi = document.querySelector('meta[name="sah-item"]'), ml = document.querySelector('meta[name="sah-list"]');
    if (mi) { var p = mi.content.split('|'); window.sahTrack('view_item', { currency: 'AED', value: +p[2] || 0, items: [{ item_id: p[0], item_name: p[1], price: +p[2] || 0, item_category: p[3] || '' }] }); }
    if (ml) window.sahTrack('view_item_list', { item_list_name: ml.content });
  });
  window.sahTrack = function (name, params) {
    if (local) return;
    params = params || {};
    try { gtag('event', name, params); var o = { event: name }; for (var k in params) o[k] = params[k]; window.dataLayer.push(o); } catch (e) {}
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a'); if (!a) return;
    var href = a.getAttribute('href') || '', t = a.getAttribute('data-track');
    var m = href.match(/book\.html\?treatment=([\w-]+)/); if (m) window.sahTrack('select_item', { items: [{ item_id: m[1] }], item_list_name: location.pathname });
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
