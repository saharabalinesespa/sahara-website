/* Sahara menu sync — keeps treatments, prices, categories and the therapist team on the site identical to the admin portal.
   Runs before site.js: a cached copy is applied instantly, then the live copy is fetched and the page updates itself.
   If the booking system cannot be reached the page simply keeps the menu it was built with. */
(function () {
  'use strict';
  var API = window.SAHARA_API, S = window.SAHARA;
  if (!API || !S) return;
  var KEY = 'sahara-menu-v3', applied = '', MENU = null;
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var esc = function (t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var num = function (n) { return (Math.round(n * 100) / 100).toLocaleString('en-US'); };
  var durLabel = function (o) { return o.length ? o.map(function (x) { return x[0]; }).join(' / ') + ' min' : ''; };
  var priceLabel = function (o) { return o.map(function (x) { return 'AED ' + num(x[1]); }).join(' / '); };
  var catItems = function (c) { return S.items.filter(function (i) { return i.cat === c; }); };
  var byId = function (id) { return S.items.filter(function (i) { return i.id === id; })[0]; };

  function apply(m) {
    var cats = {};
    m.categories.forEach(function (c) { cats[c.id] = { name: c.name }; });
    S.cats = cats;
    S.items = m.services.map(function (s) {
      return { id: s.id, name: s.name, blurb: s.blurb || '', desc: s.description || '', benefits: s.benefits || '', photo: s.photo || '', alt: s.photo_alt || '', cat: s.category_id, bookable: !!s.online_bookable, opts: s.options.map(function (o) { return [o.minutes, o.price / 100]; }) };
    });
    S.team = m.staff || null;
  }

  var imgUrl = function (p) { return p ? (p.charAt(0) === '/' ? API + p : p) : ''; };
  var pic = function (i) { return i.photo ? imgUrl(i.photo) : ((S.stock || []).indexOf(i.id) > -1 ? 'assets/services/' + i.id + '.webp' : ''); };
  function cardHtml(i) {
    var more = (S.treatmentPages || []).indexOf(i.id) > -1 ? '<span class="more">Learn more →</span>' : '<span class="more">Book →</span>';
    var href = (S.treatmentPages || []).indexOf(i.id) > -1 ? '' : 'book.html?treatment=' + encodeURIComponent(i.id);
    return '<a class="card link svc rv in" data-svc="' + esc(i.id) + '" href="' + esc(href) + '"><div class="cimg' + (pic(i) ? '' : ' empty') + '"><img data-svc-img src="' + esc(pic(i)) + '" alt="' + esc(i.alt || i.name + ' at home in Dubai') + '" loading="lazy" width="960" height="640"></div><h3 style="font-size:21px">' + esc(i.name) + '</h3><p>' + esc(i.blurb) + '</p><span class="from" data-price-svc="' + esc(i.id) + '">' + priceLabel(i.opts) + '</span>' + more + '</a>';
  }
  function rowHtml(i) {
    var im = pic(i);
    return '<tr><td class="n"><div class="rw">' + (im ? '<img class="rimg" data-svc-img data-rid="' + esc(i.id) + '" src="' + esc(im) + '" alt="' + esc(i.alt || i.name) + '" loading="lazy" width="96" height="64">' : '<span class="rimg none"></span>') + '<div><b>' + esc(i.name) + '</b><span>' + esc(i.blurb) + '</span></div></div></td><td>' + (durLabel(i.opts) || '—') + '</td><td class="p">' + priceLabel(i.opts) +
      '</td><td class="b"><a class="btn sm ghost" href="book.html?treatment=' + encodeURIComponent(i.id) + '">Book</a></td></tr>';
  }
  function tableHtml(c) {
    return '<table class="ptable" data-menu-cat="' + esc(c) + '"><thead><tr><th>Treatment</th><th>Duration</th><th>Price</th><th></th></tr></thead><tbody>' + catItems(c).map(rowHtml).join('') + '</tbody></table>';
  }

  function renderDom() {
    // price tables (price list, category pages)
    $$('table.ptable[data-menu-cat]').forEach(function (t) {
      var c = t.getAttribute('data-menu-cat'), its = catItems(c);
      t.style.display = its.length ? '' : 'none';
      var tb = t.querySelector('tbody'); if (tb && its.length) tb.innerHTML = its.map(rowHtml).join('');
    });
    // price list: headings follow renamed categories, new categories get their own section
    var groups = $$('section.pgroup');
    if (groups.length) {
      var last = groups[groups.length - 1];
      Object.keys(S.cats).forEach(function (c) {
        var g = document.getElementById(c);
        if (g && g.classList.contains('pgroup')) { var h = g.querySelector('h2'); if (h) h.textContent = S.cats[c].name; g.style.display = ''; }
        else if (!g) {
          var sec = document.createElement('section'); sec.className = 'pgroup'; sec.id = c;
          sec.innerHTML = '<h2>' + esc(S.cats[c].name) + '</h2>' + tableHtml(c); last.parentNode.insertBefore(sec, last.nextSibling); last = sec;
        }
      });
      groups.forEach(function (g) { if (!S.cats[g.id]) g.style.display = 'none'; });
    }
    // new treatments added in admin get a card in their category grid
    $$('[data-svc-grid]').forEach(function (g) {
      catItems(g.getAttribute('data-svc-grid')).forEach(function (i) {
        if (!g.querySelector('[data-svc="' + i.id + '"]')) { var d = document.createElement('div'); d.innerHTML = cardHtml(i); g.appendChild(d.firstChild); }
      });
    });
    // per-treatment cards
    $$('[data-svc]').forEach(function (card) {
      var i = byId(card.getAttribute('data-svc'));
      if (!i) { card.style.display = 'none'; return; }
      card.style.display = '';
      var h = card.querySelector('h3'), p = card.querySelector('p'), f = card.querySelector('[data-price-svc]');
      if (h) h.textContent = i.name; if (p) p.textContent = i.blurb; if (f) f.textContent = priceLabel(i.opts);
      var im = card.querySelector('img[data-svc-img]'); if (im && i.photo) { var u = imgUrl(i.photo); if (im.getAttribute('src') !== u) im.setAttribute('src', u); if (i.alt) im.alt = i.alt; }
      var cm = card.querySelector('.cimg'); if (cm && im && (i.photo || im.getAttribute('src'))) cm.classList.remove('empty');
    });
    // treatment page: photo, long description, benefits
    $$('img[data-svc-hero]').forEach(function (im) {
      var i = byId(im.getAttribute('data-svc-hero')); if (!i) return;
      if (i.photo) { var u = imgUrl(i.photo); if (im.getAttribute('src') !== u) im.setAttribute('src', u); }
      if (i.alt) im.alt = i.alt;
    });
    $$('.split [data-svc-desc]').forEach(function (p) {
      var hero = document.querySelector('img[data-svc-hero]'); var i = hero && byId(hero.getAttribute('data-svc-hero'));
      if (i && i.desc) p.textContent = i.desc;
    });
    $$('ul[data-svc-benefits]').forEach(function (ul) {
      var hero = document.querySelector('img[data-svc-hero]'); var i = hero && byId(hero.getAttribute('data-svc-hero'));
      var lines = i && i.benefits ? i.benefits.split(/\r?\n/).map(function (x) { return x.trim(); }).filter(Boolean) : [];
      if (lines.length) ul.innerHTML = lines.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('');
    });
    // treatment page price rows
    $$('tbody[data-svc-rows]').forEach(function (tb) {
      var i = byId(tb.getAttribute('data-svc-rows')); if (!i) return;
      tb.innerHTML = i.opts.map(function (o) { return '<tr><td class="n"><b>' + o[0] + ' minutes</b></td><td class="p">AED ' + num(o[1]) + '</td><td class="b"><a class="btn sm ghost" href="book.html?treatment=' + encodeURIComponent(i.id) + '">Book</a></td></tr>'; }).join('');
    });
    // "from" prices
    $$('[data-from-cat]').forEach(function (el) {
      var its = catItems(el.getAttribute('data-from-cat')); if (!its.length) return;
      var min = Math.min.apply(null, its.map(function (i) { return Math.min.apply(null, i.opts.map(function (o) { return o[1]; })); }));
      var bare = el.tagName === 'B';
      el.textContent = (bare ? '' : 'From ') + 'AED ' + num(min) + (el.hasAttribute('data-count') ? ' · ' + its.length + ' treatments' : '');
    });
    // team
    if (S.team && S.team.length) {
      $$('[data-staff-count]').forEach(function (el) { el.textContent = S.team.length; });
      var grid = document.getElementById('th-grid');
      if (grid) grid.innerHTML = S.team.map(function (t) {
        var img = !t.photo ? '' : '<img src="' + esc(t.photo.charAt(0) === '/' ? API + t.photo : t.photo) + '" alt="' + esc(t.name) + ', Sahara therapist" loading="lazy" width="600" height="750">';
        var meta = [t.experience_years ? t.experience_years + ' years experience' : '', t.languages ? 'Speaks ' + t.languages : ''].filter(Boolean).join(' · ');
        return '<div class="thc rv in"><div class="ph">' + img + '</div><h3>' + esc(t.name) + '</h3>' + (t.title ? '<span class="role">' + esc(t.title) + '</span>' : '') +
          (t.bio ? '<p style="font-size:14.5px">' + esc(t.bio) + '</p>' : '') + (meta ? '<p style="font-size:13px;opacity:.75;margin-top:8px">' + esc(meta) + '</p>' : '') +
          (t.specialties ? '<p style="font-size:13px;opacity:.75">' + esc(t.specialties) + '</p>' : '') + '</div>';
      }).join('');
    }
  }

  var cached = null; try { cached = JSON.parse(localStorage.getItem(KEY)); } catch (e) {}
  if (cached && cached.m && cached.m.services && Date.now() - cached.t < 7 * 864e5) { MENU = cached.m; apply(MENU); applied = JSON.stringify(MENU); renderDom(); }

  fetch(API + '/api/public/menu', { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : Promise.reject(); }).then(function (m) {
    if (!m || !m.services || !m.services.length) return;
    try { localStorage.setItem(KEY, JSON.stringify({ t: Date.now(), m: m })); } catch (e) {}
    var j = JSON.stringify(m); if (j === applied) return;
    applied = j; MENU = m; apply(m);
    var go = function () { renderDom(); (window.sahHooks || []).forEach(function (f) { try { f(); } catch (e) {} }); };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
  }).catch(function () {});
})();
