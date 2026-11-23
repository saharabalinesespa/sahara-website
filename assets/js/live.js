/* Sahara live booking layer. Loaded ONLY when the site is built with a backend URL (SAHARA_API).
   It upgrades the existing book / gift-voucher pages in place; if the API is unreachable the WhatsApp flow keeps working. */
(function () {
  'use strict';
  var API = (window.SAHARA_API || '').replace(/\/$/, '');
  if (!API) return;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var aed = function (f) { var v = f / 100; return 'AED ' + (v % 1 ? v.toFixed(2) : v.toLocaleString('en-US')); };
  function api(method, path, body) {
    return fetch(API + path, { method: method, headers: body ? { 'content-type': 'application/json' } : {}, body: body ? JSON.stringify(body) : undefined })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { if (!r.ok) { var e = new Error(d.error || 'Something went wrong'); e.status = r.status; throw e; } return d; }); });
  }
  var t12 = function (t) { var p = t.split(':'), h = +p[0], ap = h >= 12 ? 'pm' : 'am'; h = h % 12 || 12; return h + ':' + p[1] + ' ' + ap; };
  var niceDate = function (d) { return new Date(d.slice(0, 10) + 'T00:00:00Z').toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }); };
  var T = function (n, p) { try { window.sahTrack && window.sahTrack(n, p || {}); } catch (e) {} };
  var AGREE = '<div class="agree"><label><input type="checkbox" id="@ID@"> <span>I agree to the <a href="terms-conditions.html" target="_blank" rel="noopener">Terms</a>, the <a href="payments-refunds.html" target="_blank" rel="noopener">Payments &amp; Refunds Policy</a> and the <a href="privacy-policy.html" target="_blank" rel="noopener">Privacy Policy</a>.</span></label><p class="paynote">@NOTE@</p></div>';
  var catalogP = null;
  function catalog() { return catalogP || (catalogP = api('GET', '/api/public/catalog')); }

  /* ---------------- booking page ---------------- */
  function initBooking(cat) {
    var form = $('#bk-form'); if (!form) return;
    var svcById = {}; cat.services.forEach(function (s) { svcById[s.id] = s; });
    var timeSel = $('#time'), dateEl = $('#date'), est = $('#est-total'), estN = $('#est-note'), err = $('#bk-err');
    // extra fields
    $('#wnum').insertAdjacentHTML('afterend', '<label for="wemail">Email (booking confirmation)</label><input id="wemail" type="email" autocomplete="email" placeholder="you@example.com">');
    timeSel.closest('.frow').insertAdjacentHTML('afterend', '<div id="pref-wrap" class="hide"><label for="wstaff">Therapist preference (optional)</label><select id="wstaff"></select></div>');
    var btn = $('.est .btn'); btn.textContent = 'Confirm booking'; btn.classList.remove('wa');
    var payNote = (cat.payments_enabled && cat.policy.deposit_mode !== 'none') ? 'Your deposit is paid on Network International’s secure page (Visa / Mastercard). Sahara never sees or stores your card details.' : 'No payment is taken online. You pay after your treatment.';
    $('.est').insertAdjacentHTML('beforebegin', AGREE.replace('@ID@', 'bk-terms').replace('@NOTE@', payNote));
    var info = document.createElement('p'); info.id = 'live-info'; info.style.cssText = 'font-size:13.5px;margin-top:12px'; $('.est').parentNode.insertBefore(info, $('#bk-err'));
    var busy = false, last = 0;
    var fs = { started: false, quoted: false, time: false, submitted: false, gone: false };
    var ec = function (x) { return { currency: 'AED', value: x.opt.price / 100 * x.guests, items: [{ item_id: x.s.id, item_name: x.s.name, item_category: x.s.category || '', price: x.opt.price / 100, quantity: x.guests }] }; };
    form.addEventListener('focusin', function () { if (!fs.started) { fs.started = true; T('booking_form_start', { page: location.pathname }); } });
    timeSel.addEventListener('change', function () { var x = sel(); if (timeSel.value && x && !x.missing && !fs.time) { fs.time = true; var e = ec(x); e.shipping_tier = 'home_service'; T('add_shipping_info', e); } });
    function leave() { if (fs.quoted && !fs.submitted && !fs.gone) { fs.gone = true; T('booking_abandon', { stage: fs.time ? 'details' : 'service_or_time', missing: window.sahCheck ? window.sahCheck.missing().join(',') : '', transport_type: 'beacon' }); } }
    window.addEventListener('pagehide', leave); document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') leave(); });
    // date picker: min today (Dubai), max 1 year, opens on click anywhere in the field
    var dnow = new Date(Date.now() + 4 * 3600e3), pad = function (n) { return (n < 10 ? '0' : '') + n; };
    dateEl.min = dnow.getUTCFullYear() + '-' + pad(dnow.getUTCMonth() + 1) + '-' + pad(dnow.getUTCDate());
    dateEl.max = (dnow.getUTCFullYear() + 1) + '-' + pad(dnow.getUTCMonth() + 1) + '-' + pad(dnow.getUTCDate());
    dateEl.style.colorScheme = 'dark'; dateEl.style.cursor = 'pointer';
    dateEl.addEventListener('click', function () { try { dateEl.showPicker(); } catch (e) {} });

    function sel() {
      var tx = $('#tx-opts .opt.on'); if (!tx) return null;
      var s = svcById[tx.dataset.id]; if (!s) return { missing: true, id: tx.dataset.id };
      var d = $('#dur-opts .opt.on'); var idx = d ? +d.dataset.d : 0;
      var opt = s.options[Math.min(idx, s.options.length - 1)];
      var gOn = $('[data-g].on'), g = gOn ? +gOn.dataset.g : 1; if (g === 3) g = Math.max(3, Math.min(20, +$('#grp').value || 3));
      return { s: s, opt: opt, guests: g };
    }
    function fillStaff(s, guests) {
      var wrap = $('#pref-wrap'), sel2 = $('#wstaff'); var keep = sel2.value;
      var list = cat.staff.filter(function (st) { return st.services.indexOf(s.id) > -1; });
      if (s.staff_count > 1 || guests > 1 || list.length < 2) { wrap.classList.add('hide'); sel2.innerHTML = '<option value="">Any available therapist</option>'; return; }
      sel2.innerHTML = '<option value="">Any available therapist</option>' + list.map(function (st) { return '<option value="' + st.id + '">' + esc(st.name) + '</option>'; }).join('');
      sel2.value = keep; wrap.classList.remove('hide');
    }
    function refresh() {
      var x = sel(); err.textContent = '';
      if (!x) return;
      if (x.missing) { info.textContent = 'This service is booked by request — please use WhatsApp or the contact page.'; timeSel.innerHTML = '<option value="">—</option>'; return; }
      fillStaff(x.s, x.guests); info.textContent = '';
      api('POST', '/api/public/quote', { options: [x.opt.id], guests: x.guests, date: dateEl.value || undefined }).then(function (q) {
        est.textContent = aed(q.total); estN.textContent = x.s.name + (x.opt.minutes ? ' · ' + x.opt.minutes + ' min' : '') + ' · ' + x.guests + ' guest' + (x.guests > 1 ? 's' : '') + ' · VAT included';
        if (!fs.quoted) { fs.quoted = true; T('begin_checkout', ec(x)); }
        var dep = cat.policy.deposit_mode; if (cat.payments_enabled && dep !== 'none') {
          var amt = dep === 'percent' ? Math.round(q.total * cat.policy.deposit_value / 100) : cat.policy.deposit_value * 100;
          info.textContent = 'A deposit of ' + aed(Math.min(amt, q.total)) + ' is paid online to confirm your booking; the balance is paid after your treatment.';
        }
      }).catch(function () {});
      if (!dateEl.value) return;
      var my = ++last; var qs = 'date=' + dateEl.value + '&options=' + x.opt.id + '&guests=' + x.guests; var st = $('#wstaff').value; if (st) qs += '&staff=' + st;
            api('GET', '/api/public/availability?' + qs).then(function (r) {
        if (my !== last) return; var prev = timeSel.value;
        var html = r.slots.length ? '<option value="">Choose a time</option>' + r.slots.map(function (s) { return '<option value="' + s.time + '">' + t12(s.time) + '</option>'; }).join('') : '<option value="">No times free on this date</option>';
        if (timeSel.dataset.h !== html) { timeSel.dataset.h = html; timeSel.innerHTML = html; if (prev) timeSel.value = prev; }
      }).catch(function () { timeSel.innerHTML = '<option value="">Could not load times</option>'; });
    }
    var tmr; var soon = function () { clearTimeout(tmr); tmr = setTimeout(refresh, 60); };
    document.addEventListener('click', function (e) { if (e.target.closest('#booking') && e.target.closest('.opt,[data-g],.stepper,button') && !e.target.closest('select,input')) soon(); }, true);
    dateEl.addEventListener('change', soon); dateEl.addEventListener('input', soon); $('#grp').addEventListener('input', soon); $('#wstaff').addEventListener('change', soon);
    timeSel.innerHTML = '<option value="">Choose a date first</option>';
    soon();

    document.addEventListener('submit', function (e) {
      if (e.target !== form) return;
      e.preventDefault(); e.stopImmediatePropagation();
      if (busy) return;
      var x = sel(), v = function (id) { return ($('#' + id).value || '').trim(); };
      var miss = window.sahCheck ? window.sahCheck.missing().join(',') : '';
      if (window.sahCheck && window.sahCheck.run(true)) { T('booking_blocked', { missing: miss }); return; }
      if (!x || x.missing) { err.textContent = 'Please choose a treatment that can be booked online, or contact us on WhatsApp.'; return; }
      if (!dateEl.value || !v('time')) { err.textContent = 'Please choose a date and an available time.'; return; }
      if (!v('fn') || !v('wnum')) { err.textContent = 'Please add your name and mobile number.'; return; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('wemail'))) { err.textContent = 'Please add a valid email — your confirmation is sent there.'; return; }
      if (!v('bldg') && !v('pin')) { err.textContent = 'Please add your building/community or a Google Maps pin.'; return; }
      err.textContent = ''; busy = true; btn.disabled = true; btn.textContent = 'Booking…';
      api('POST', '/api/public/book', { date: dateEl.value, time: v('time'), options: [x.opt.id], guests: x.guests, name: (v('fn') + ' ' + v('ln')).trim(), phone: v('wnum'), email: v('wemail'),
        building: v('bldg'), unit: v('apt'), map_link: v('pin'), notes: [v('notes'), v('heard') ? 'Heard about us: ' + v('heard') : ''].filter(Boolean).join(' | '), staff_id: v('wstaff') || undefined, website: '', accept_terms: $('#bk-terms').checked })
        .then(function (r) {
          fs.submitted = true; var e = ec(x); T('booking_submitted', e);
          var go = r.pay_url ? r.pay_url : 'booking-confirmed.html?status=' + encodeURIComponent(r.status) + '&t=' + encodeURIComponent(r.token);
          if (r.pay_url) { e.payment_type = 'card_network_international'; T('add_payment_info', e); T('payment_redirect', { transaction_id: r.ref, value: r.deposit / 100, currency: 'AED', transport_type: 'beacon' }); }
          setTimeout(function () { location.href = go; }, 250); })
        .catch(function (ex) { err.textContent = ex.message; T('booking_error', { reason: String(ex.message || '').slice(0, 60), status: ex.status || 0 }); if (ex.status === 409) { T('slot_unavailable'); refresh(); } busy = false; btn.disabled = false; btn.textContent = 'Confirm booking'; });
    }, true);
  }

  /* ---------------- gift voucher page ---------------- */
  function initVoucher(cat) {
    var form = $('#v-form'); if (!form || !cat.payments_enabled) return;   // payments off => keep the WhatsApp request flow
    var err = $('#v-err'), busy = false, btn = $('.est .btn', form);
    $('#v-email').previousElementSibling.textContent = 'Your email (voucher & receipt sent here)';
    $('#v-to').closest('.frow').insertAdjacentHTML('afterend', '<label for="v-remail">Recipient’s email (we email the voucher to them)</label><input id="v-remail" type="email" placeholder="optional — leave blank to receive it yourself">');
    $('#v-del').innerHTML = '<option>Email the voucher to me</option><option>Email the voucher to the recipient</option>';
    btn.textContent = 'Pay securely'; btn.classList.remove('wa');
    $('.est', form).insertAdjacentHTML('beforebegin', AGREE.replace('@ID@', 'v-terms').replace('@NOTE@', 'You pay on Network International’s secure page (Visa / Mastercard). Sahara never sees or stores your card details. Vouchers are valid for 12 months and are non-refundable once issued.'));
    var vs = { quoted: false, submitted: false, gone: false }, vtot = $('#v-total');
    var vval = function () { return parseFloat((vtot.textContent || '').replace(/[^\d.]/g, '')) || 0; };
    var vec = function () { return { currency: 'AED', value: vval(), items: [{ item_id: 'gift_voucher', item_name: 'Gift voucher', item_category: 'voucher', price: vval(), quantity: 1 }] }; };
    new MutationObserver(function () { if (!vs.quoted && vval() > 0) { vs.quoted = true; T('begin_checkout', vec()); } }).observe(vtot, { childList: true, characterData: true, subtree: true });
    function vleave() { if (vs.quoted && !vs.submitted && !vs.gone) { vs.gone = true; T('voucher_abandon', { transport_type: 'beacon' }); } }
    window.addEventListener('pagehide', vleave); document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') vleave(); });
    document.addEventListener('submit', function (e) {
      if (e.target !== form) return; e.preventDefault(); e.stopImmediatePropagation(); if (busy) return;
      var v = function (id) { return ($('#' + id).value || '').trim(); };
      var amount = parseFloat(($('#v-total').textContent || '').replace(/[^\d.]/g, '')) || 0;
      if (!amount) { err.textContent = 'Please choose a treatment or enter an amount.'; return; }
      if (amount < cat.vouchers.min_amount || amount > cat.vouchers.max_amount) { err.textContent = 'Voucher value must be between AED ' + cat.vouchers.min_amount + ' and AED ' + cat.vouchers.max_amount + '.'; return; }
      if (!v('v-name') || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('v-email'))) { err.textContent = 'Please add your name and a valid email.'; T('booking_blocked', { form: 'voucher', missing: 'name_or_email' }); return; }
      if (!$('#v-terms').checked) { err.textContent = 'Please tick the agreement to continue.'; T('booking_blocked', { form: 'voucher', missing: 'terms' }); return; }
      var toRecipient = $('#v-del').selectedIndex === 1; if (toRecipient && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('v-remail'))) { err.textContent = 'Please add the recipient’s email.'; return; }
      err.textContent = ''; busy = true; btn.disabled = true; btn.textContent = 'Please wait…';
      api('POST', '/api/public/voucher/buy', { amount: amount, purchaser_name: v('v-name'), purchaser_phone: v('v-phone'), purchaser_email: v('v-email'), recipient_name: v('v-to'),
        recipient_email: toRecipient ? v('v-remail') : '', occasion: $('#v-occ').value, message: v('v-msg'), website: '', accept_terms: true })
        .then(function (r) { vs.submitted = true; var e = vec(); e.payment_type = 'card_network_international'; T('add_payment_info', e); T('payment_redirect', { value: amount, currency: 'AED', form: 'voucher', transport_type: 'beacon' }); setTimeout(function () { location.href = r.pay_url; }, 250); })
        .catch(function (ex) { err.textContent = ex.message; T('booking_error', { form: 'voucher', reason: String(ex.message || '').slice(0, 60) }); busy = false; btn.disabled = false; btn.textContent = 'Pay securely'; });
    }, true);
  }

  /* ---------------- confirmation + manage pages ---------------- */
  var REVIEW = 'https://g.page/r/CYgduMaDQaJUEAI/review';
  function reviewPanel(done, tok) {
    return '<div class="panel" style="margin-top:16px"><div aria-hidden="true" style="color:var(--gold);font-size:22px;letter-spacing:5px">★★★★★</div><h3 class="st" style="margin-top:6px">' + (done ? 'How was your treatment?' : 'After your treatment') + '</h3><p>' +
      (done ? 'Thank you for choosing Sahara. Your Google review takes under a minute and helps others find us.' : 'We would be grateful for 30 seconds of your time — a Google review helps other families and professionals in Dubai find a trusted home spa.') +
      '</p><div class="btns">' + (done && tok ? '<a class="btn" href="feedback.html?t=' + encodeURIComponent(tok) + '" data-track="feedback_open">Rate your treatment</a><a class="btn ghost" href="' + REVIEW + '" target="_blank" rel="noopener" data-track="review_click">Leave a Google review</a>' : '<a class="btn" href="' + REVIEW + '" target="_blank" rel="noopener" data-track="review_click">Leave a Google review</a>') + '</div></div>';
  }
  function once(key, fn) { try { if (sessionStorage.getItem(key)) return; sessionStorage.setItem(key, '1'); } catch (e) {} fn(); }
  function apptHtml(a) {
    return '<div class="panel"><h2 style="margin-bottom:14px">' + esc(a.ref) + ' <span class="pill" style="font-size:12px;border:1px solid var(--gold);padding:2px 10px;border-radius:99px">' + esc(a.status.replace('_', ' ')) + '</span></h2>' +
      '<p><b>' + esc(niceDate(a.starts_at)) + '</b> at <b>' + t12(a.starts_at.slice(11)) + '</b></p>' +
      '<ul class="ticks">' + a.items.map(function (i) { return '<li>' + esc(i.name) + (i.qty > 1 ? ' × ' + i.qty : '') + '</li>'; }).join('') + '</ul>' +
      '<p>' + esc([a.building, a.unit].filter(Boolean).join(', ')) + '</p>' +
      '<p>Total <b>' + aed(a.total) + '</b> (VAT included)' + (a.deposit_required ? ' · deposit ' + aed(a.deposit_required) + (a.deposit_paid ? ' paid' : ' due') : '') + '</p></div>';
  }
  function initConfirm() {
    var box = $('#bk-confirm'); if (!box) return;
    var q = new URLSearchParams(location.search), st = q.get('status'), t = q.get('t'), kind = q.get('kind'), ref = q.get('ref') || '', amt = +(q.get('amt') || 0);
    var retry = kind === 'voucher' ? 'gift-vouchers.html' : (t ? 'booking-manage.html?t=' + encodeURIComponent(t) : 'book.html');
    function stage(name, extra) { once('sah-' + name + '-' + (ref || t || 'x'), function () { var p = { transaction_id: ref, kind: kind || 'deposit' }; for (var k in (extra || {})) p[k] = extra[k]; T(name, p); }); }
    if (st === 'failed' || st === 'cancelled' || st === 'unknown') {
      stage(st === 'cancelled' ? 'payment_cancelled' : 'payment_failed', { value: amt / 100, currency: 'AED' });
      var why = st === 'cancelled' ? 'You left the payment page, so no money was taken.' : 'The payment was not completed, so no money was taken.';
      box.innerHTML = '<div class="panel"><h2>Payment not completed</h2><p>' + why + (kind === 'voucher' ? '' : ' Your booking is not confirmed yet, but your time is held for a short while.') + '</p><div class="btns"><a class="btn" href="' + retry + '">' + (kind === 'voucher' ? 'Try again' : (t ? 'Review booking and pay' : 'Book again')) + '</a><a class="btn ghost" href="' + 'https://wa.me/971502052017' + '" target="_blank" rel="noopener">Need help? WhatsApp us</a></div><p style="font-size:13px;opacity:.8">Having card problems? Try another Visa or Mastercard, or ask your bank to approve the payment.</p></div>';
      return;
    }
    if (kind === 'voucher') {
      if (st === 'paid') { stage('purchase', { value: amt / 100, currency: 'AED', items: [{ item_id: 'gift_voucher', item_name: 'Gift voucher', item_category: 'voucher', price: amt / 100, quantity: 1 }] }); box.innerHTML = '<div class="panel"><h2>Thank you — payment received</h2><p>Your gift voucher is being emailed now. Check your inbox (and spam folder). Reference ' + esc(ref) + '.</p></div>'; }
      else { stage('payment_pending', { value: amt / 100, currency: 'AED' }); box.innerHTML = '<div class="panel"><h2>We are confirming your payment</h2><p>Your bank is still processing it. You will receive the voucher by email as soon as it is confirmed — usually within minutes.</p></div>'; }
      return;
    }
    if (!t) { box.innerHTML = '<div class="panel"><p>We could not find that booking. Please contact us on WhatsApp.</p></div>'; return; }
    var tries = 0;
    function load() {
      api('GET', '/api/public/appointment/' + encodeURIComponent(t)).then(function (a) {
        if (a.status === 'pending' && st === 'pending' && tries++ < 6) { box.innerHTML = '<div class="panel"><h2>Confirming your payment…</h2><p>Please keep this page open for a moment while we verify it with the bank.</p></div>'; setTimeout(load, 5000); return; }
        box.innerHTML = '<div class="panel"><h2>' + (a.status === 'pending' ? 'Almost there' : 'You’re booked, ' + esc(a.client_name.split(' ')[0])) + '</h2><p>' + (a.status === 'pending' ? 'We are waiting for your deposit to confirm this booking. If you were charged, you will receive your confirmation by email within minutes.' : 'A confirmation has been emailed to you. Our therapist will arrive at the time below.') + '</p></div>' + apptHtml(a) +
          '<div class="btns"><a class="btn" href="booking-manage.html?t=' + encodeURIComponent(t) + '">Manage or cancel</a></div>';
        if (a.status === 'pending') { stage('payment_pending', { value: amt / 100, currency: 'AED' }); return; }
        box.innerHTML += reviewPanel(false);
        once('sah-bk-' + a.ref, function () {
          T('booking_confirmed', { transaction_id: a.ref, value: a.total / 100, currency: 'AED', deposit_paid: !!a.deposit_paid });
          if (st === 'paid') T('purchase', { transaction_id: a.ref, value: (amt || a.deposit_paid) / 100, currency: 'AED', items: a.items.map(function (i) { return { item_id: i.name, item_name: i.name, price: i.price / 100, quantity: i.qty || 1 }; }) });
        });
      }).catch(function (ex) { box.innerHTML = '<div class="panel"><p>' + esc(ex.message) + '</p></div>'; });
    }
    load();
  }
  function initManage() {
    var box = $('#bk-manage'); if (!box) return;
    var t = new URLSearchParams(location.search).get('t'); if (!t) { box.innerHTML = '<div class="panel"><p>Open this page from the link in your confirmation email.</p></div>'; return; }
    api('GET', '/api/public/appointment/' + encodeURIComponent(t)).then(function (a) {
      var html = apptHtml(a);
      if (a.can_cancel) {
        var p = a.cancel_preview, msg = p.late ? 'This is inside the late-cancellation window, so a fee of <b>' + aed(p.fee) + '</b> applies' + (p.retained ? ' (your deposit covers it)' : '') + '.' : 'Free to cancel right now.';
        if (!p.late && p.refund) msg += ' Your deposit of ' + aed(p.refund) + ' will be refunded.';
        html += '<div class="panel"><h3 class="st">Need to cancel?</h3><p>' + msg + '</p><button class="btn" id="cx">Cancel this booking</button><p class="err" id="cx-err"></p></div><p style="font-size:14px">To change the time, please <a href="contact.html">contact us</a> — we will move it for you.</p>';
      }
      html += reviewPanel(a.status === 'completed', t);
      box.innerHTML = html;
      var b = $('#cx'); if (b) b.addEventListener('click', function () {
        if (!confirm('Cancel this booking?')) return; b.disabled = true;
        api('POST', '/api/public/appointment/' + encodeURIComponent(t) + '/cancel').then(function () { location.reload(); }).catch(function (ex) { $('#cx-err').textContent = ex.message; b.disabled = false; });
      });
    }).catch(function (ex) { box.innerHTML = '<div class="panel"><p>' + esc(ex.message) + '</p></div>'; });
  }


  /* ---------------- guest feedback ---------------- */
  function initFeedback() {
    var box = $('#fb-box'); if (!box) return;
    var t = new URLSearchParams(location.search).get('t');
    if (!t) { box.innerHTML = '<div class="panel"><p>Please open this page from the link in your email.</p></div>'; return; }
    function thanks(g, rating) {
      box.innerHTML = '<div class="panel"><h3 class="st">Thank you' + '</h3><p>We have received your feedback' + (rating <= 3 ? ' and our team will personally follow up if needed.' : '.') + '</p>' +
        (g ? '<p>If you would like to share your experience publicly, a Google review helps other guests find us. It is entirely optional.</p><div class="btns"><a class="btn" href="' + esc(g) + '" target="_blank" rel="noopener" data-track="review_click">Leave a Google review</a></div>' : '') + '</div>';
    }
    api('GET', '/api/public/feedback/' + encodeURIComponent(t)).then(function (f) {
      if (f.done) return thanks(f.google_url, f.rating);
      var rating = 0;
      box.innerHTML = '<div class="panel"><h3 class="st">Hi ' + esc(f.first_name) + ', how was it?</h3><p>' + esc(f.items.join(', ')) + (f.staff.length ? ' with ' + esc(f.staff.join(' & ')) : '') + '</p>' +
        '<div id="fb-stars" role="radiogroup" aria-label="Rating" style="display:flex;gap:6px;margin:14px 0">' + [1, 2, 3, 4, 5].map(function (n) { return '<button type="button" class="fb-star" role="radio" aria-checked="false" aria-label="' + n + ' star' + (n > 1 ? 's' : '') + '" data-n="' + n + '" style="background:none;border:0;font-size:38px;line-height:1;color:var(--line,#555);cursor:pointer;padding:4px 6px;min-width:44px;min-height:44px">★</button>'; }).join('') + '</div>' +
        '<label for="fb-c">Anything you would like to tell us? (optional)</label><textarea id="fb-c" rows="4" maxlength="600"></textarea>' +
        '<label id="fb-consent" style="display:none;gap:10px;align-items:flex-start;margin:12px 0"><input type="checkbox" id="fb-ok" style="width:auto;margin-top:4px"> <span>You may show my comment and first name on the Sahara website.</span></label>' +
        '<p style="font-size:12.5px;opacity:.8">We only use your first name and comment if you tick the box above. Your contact details are never shown.</p>' +
        '<div class="btns"><button class="btn" id="fb-go" disabled>Send feedback</button></div><p class="err" id="fb-err" role="alert"></p></div>';
      var stars = $$('.fb-star', box), go = $('#fb-go'), c = $('#fb-c'), cons = $('#fb-consent');
      function paint() { stars.forEach(function (s) { var on = +s.dataset.n <= rating; s.style.color = on ? 'var(--gold,#DBA83C)' : 'var(--line,#555)'; s.setAttribute('aria-checked', on && +s.dataset.n === rating ? 'true' : 'false'); }); go.disabled = !rating; }
      stars.forEach(function (s) { s.addEventListener('click', function () { rating = +s.dataset.n; paint(); }); });
      c.addEventListener('input', function () { cons.style.display = c.value.trim() ? 'flex' : 'none'; });
      go.addEventListener('click', function () {
        go.disabled = true; $('#fb-err').textContent = '';
        api('POST', '/api/public/feedback/' + encodeURIComponent(t), { rating: rating, comment: c.value, consent: $('#fb-ok').checked }).then(function (r) {
          window.sahTrack && window.sahTrack('feedback_submitted', { rating: rating });
          thanks(r.google_url, rating);
        }).catch(function (ex) { $('#fb-err').textContent = ex.message; go.disabled = false; });
      });
    }).catch(function (ex) { box.innerHTML = '<div class="panel"><p>' + esc(ex.message) + '</p></div>'; });
  }
  function initTestimonials() {
    var home = $('#gf-home'), rev = $('#gf-reviews'); if (!home && !rev) return;
    api('GET', '/api/public/testimonials').then(function (d) {
      if (!d.items.length) return;
      var card = function (i) { return '<figure class="gf-card"><div aria-label="' + i.rating + ' out of 5" style="color:var(--gold);letter-spacing:3px">' + '★'.repeat(i.rating) + '<span style="opacity:.3">' + '★'.repeat(5 - i.rating) + '</span></div><blockquote>' + esc(i.comment) + '</blockquote><figcaption>' + esc(i.name) + (i.service ? ' · ' + esc(i.service) : '') + '<small>' + (i.source === 'site' ? 'Verified Sahara booking' : i.source === 'google' ? 'From a Google review' : 'Guest message') + '</small></figcaption></figure>'; };
      function fill(sec, items, sum) {
        $('.gf-grid', sec).innerHTML = items.map(card).join(''); sec.hidden = false;
        var s = $('.gf-sum', sec); if (s && sum) s.textContent = 'Average ' + d.average.toFixed(1) + ' / 5 from ' + d.count + ' rating' + (d.count === 1 ? '' : 's') + ' on our own booking feedback';
        var n = $('.gf-note', sec); if (n) n.textContent = 'Shown with each guest’s permission. First names only.';
      }
      if (home) fill(home, d.items.slice(0, 3), false);
      if (rev) fill(rev, d.items, true);
    }).catch(function () { /* API down: sections stay hidden */ });
  }

  initConfirm(); initManage(); initFeedback(); initTestimonials();
  if ($('#bk-form') || $('#v-form')) catalog().then(function (cat) { initBooking(cat); initVoucher(cat); }).catch(function () { /* API down: legacy WhatsApp flow stays active */ });
})();
