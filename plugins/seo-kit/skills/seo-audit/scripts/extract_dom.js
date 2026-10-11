/*
 * seo-kit · extract_dom.js
 *
 * Reads the RENDERED DOM (after JavaScript) and returns the same page keys as
 * seo_fetch.py reads from the raw server HTML (see docs/page-schema.md for the
 * keys and the few that differ), so the two can be compared field by field.
 * Extra keys only available in a browser: clickable_non_links,
 * css_background_images, hash_routing_links, hidden_text_containers.
 *
 * Usage
 *   Chrome DevTools MCP: pass the arrow function below verbatim (from `() => {`
 *   to the final `}`, without this comment) as the `function` argument:
 *     evaluate_script({ function: "<the arrow function below, unchanged>" })
 *   Browser console: run it as an immediately invoked function:
 *     (() => { ...body of the function below... })()
 *   or the older form:
 *     (function () { ...body of the function below... })()
 */
() => {
  const doc = document;
  const pageUrl = location.href;
  const body = doc.body || null;
  const q = (selector, root) => Array.from((root || doc).querySelectorAll(selector));
  const clean = (s) => String(s || '').replace(/\s+/g, ' ').trim();
  const toUrl = (href, base) => {
    try {
      return new URL(href, base || doc.baseURI || pageUrl);
    } catch (e) {
      return null;
    }
  };
  const DOC_RE = /\.(pdf|docx?|pptx?|xlsx?|odt|ods|odp|rtf)$/i;
  const HREFLANG_RE = /^(x-default|[a-z]{2,3}(-[a-z]{4})?(-([a-z]{2}|\d{3}))?)$/i;
  const LANG_MISTAKES = { jp: 'ja', cn: 'zh', gr: 'el', dk: 'da', cz: 'cs', kr: 'ko', ua: 'uk' };
  const REGION_MISTAKES = { uk: 'gb', eu: null };
  const ROBOTS_NAMES = ['robots', 'googlebot', 'bingbot', 'googlebot-news'];
  const NON_MAIN = 'nav, header, footer, aside';

  const inForeign = (el) => !!(el.closest && el.closest('svg, math'));
  const schemeOf = (href) => {
    const m = /^\s*([a-z][a-z0-9+.\-]*):/i.exec(href || '');
    return m ? m[1].toLowerCase() : '';
  };
  const siteKey = (u) => {
    let host = (u.hostname || '').toLowerCase();
    if (host.startsWith('www.')) host = host.slice(4);
    return u.port ? host + ':' + u.port : host; // URL.port is '' for the default port
  };
  const compareKey = (href) => {
    const u = toUrl(href);
    if (!u) return String(href || '');
    let path = u.pathname;
    if (path.length > 1 && path.endsWith('/')) path = path.replace(/\/+$/, '') || '/';
    if (path === '/') path = '';
    return u.protocol + '//' + u.host.toLowerCase() + path + u.search;
  };
  const textOf = (el) => {
    // Text without <svg>/<math> descendants (an SVG <title> is not a heading).
    const copy = el.cloneNode(true);
    copy.querySelectorAll('svg, math, script, style, template, noscript').forEach((n) => n.remove());
    return clean(copy.textContent);
  };
  const metaByName = (name) =>
    q('meta').filter((m) => (m.getAttribute('name') || m.getAttribute('property') || '').toLowerCase() === name);

  // -- head ---------------------------------------------------------------
  const title = q('title').filter((t) => !inForeign(t)).map((t) => clean(t.textContent));
  const meta_description = metaByName('description').map((m) => clean(m.getAttribute('content')));
  const robots_meta = {};
  for (const name of ROBOTS_NAMES) {
    const values = metaByName(name).map((m) => clean(m.getAttribute('content')));
    if (values.length) robots_meta[name] = values;
  }
  const viewportMeta = metaByName('viewport')[0];
  const viewport = viewportMeta ? clean(viewportMeta.getAttribute('content')) : null;
  const og = {};
  const twitter = {};
  for (const m of q('meta')) {
    const key = (m.getAttribute('property') || m.getAttribute('name') || '').toLowerCase();
    const content = clean(m.getAttribute('content'));
    if (key.startsWith('og:') && !(key in og)) og[key] = content;
    if (key.startsWith('twitter:') && !(key in twitter)) twitter[key] = content;
  }
  const baseEl = doc.querySelector('base[href]');
  const base_href = baseEl ? doc.baseURI : null;
  const lang = doc.documentElement.getAttribute('lang') || null;

  const canonLinks = q('link[rel]').filter((l) => l.getAttribute('rel').toLowerCase().split(/\s+/).includes('canonical'));
  const headCanon = canonLinks.filter((l) => !(body && body.contains(l)));
  const chosen = headCanon[0] || canonLinks[0] || null;
  const canonical = {
    href: chosen ? chosen.getAttribute('href') : null,
    resolved: null,
    self_referencing: null,
    in_body: canonLinks.length > 0 && headCanon.length === 0,
    count: canonLinks.length,
    all: canonLinks.map((l) => l.getAttribute('href')),
  };
  if (chosen && clean(chosen.getAttribute('href'))) {
    const u = toUrl(chosen.getAttribute('href'));
    canonical.resolved = u ? u.href : null;
    canonical.self_referencing = u ? compareKey(u.href) === compareKey(pageUrl) : null;
  }

  const validCode = (code) => {
    code = clean(code);
    if (!HREFLANG_RE.test(code)) return false;
    if (code.toLowerCase() === 'x-default') return true;
    const parts = code.toLowerCase().split('-');
    if (parts[0] in LANG_MISTAKES) return false;
    const region = parts.length > 1 && parts[parts.length - 1].length === 2 ? parts[parts.length - 1] : null;
    return !(region && region in REGION_MISTAKES);
  };
  const hreflang = q('link[hreflang]')
    .filter((l) => (l.getAttribute('rel') || '').toLowerCase().split(/\s+/).includes('alternate'))
    .map((l) => {
      const u = toUrl(l.getAttribute('href') || '');
      return { lang: clean(l.getAttribute('hreflang')), href: l.getAttribute('href'),
        resolved: u ? u.href : null, valid_code: validCode(l.getAttribute('hreflang')) };
    });
  const hreflang_issues = [];
  const seenCodes = {};
  for (const h of hreflang) {
    if (!h.valid_code) hreflang_issues.push({ issue: 'invalid_code', detail: h.lang });
    const key = h.lang.toLowerCase();
    const target = compareKey(h.resolved || '');
    if (key in seenCodes && seenCodes[key] !== target) {
      hreflang_issues.push({ issue: 'duplicate_code', detail: h.lang + ' points to more than one URL' });
    }
    if (!(key in seenCodes)) seenCodes[key] = target;
  }
  if (hreflang.length && !hreflang.some((h) => compareKey(h.resolved || '') === compareKey(pageUrl))) {
    hreflang_issues.push({ issue: 'missing_self_reference', detail: 'the hreflang set does not include this page' });
  }

  // -- headings -------------------------------------------------------------
  const headings = q('h1, h2, h3, h4, h5, h6')
    .filter((h) => !inForeign(h))
    .map((h) => ({ level: Number(h.tagName.slice(1)), text: textOf(h) }));
  const h1 = headings.filter((h) => h.level === 1).map((h) => h.text);
  const heading_skips = [];
  let prev = 0;
  for (const h of headings) {
    if (prev && h.level > prev + 1) heading_skips.push({ from: 'h' + prev, to: 'h' + h.level, text: h.text.slice(0, 100) });
    prev = h.level;
  }

  // -- links ----------------------------------------------------------------
  const pageSite = siteKey(toUrl(pageUrl) || { hostname: location.hostname, port: location.port });
  const internal_links = [];
  const external_links = [];
  const other_links = {};
  const documents = [];
  const hashRouting = new Set();
  for (const a of q('a[href]')) {
    if (inForeign(a)) continue;
    const href = clean(a.getAttribute('href'));
    if (!href) continue;
    if (/^#[!/]/.test(href)) hashRouting.add(href);
    // mailto: tel: sms: whatsapp: javascript: data: ftp: (and any other non-http scheme) are
    // neither internal nor external; counted per scheme (case-insensitive), like seo_fetch.py.
    const kind = href.startsWith('#') ? 'fragment' : schemeOf(href);
    if (kind === 'fragment' || (kind && kind !== 'http' && kind !== 'https')) {
      other_links[kind] = (other_links[kind] || 0) + 1;
      continue;
    }
    const u = toUrl(href);
    if (!u) {
      other_links.invalid = (other_links.invalid || 0) + 1;
      continue;
    }
    const rel = (a.getAttribute('rel') || '').toLowerCase().split(/\s+/).filter(Boolean);
    const imgAlt = q('img[alt]', a).map((i) => i.getAttribute('alt')).join(' ');
    const link = { href, resolved: u.href, text: clean(a.innerText || a.textContent) || clean(imgAlt), rel,
      nofollow: rel.includes('nofollow') };
    if (DOC_RE.test(u.pathname) && !documents.includes(u.href)) documents.push(u.href);
    (siteKey(u) === pageSite ? internal_links : external_links).push(link);
  }
  const anchors_without_href = q('a:not([href])').length;
  // Framework router attributes are hints: without a real <a href> crawlers cannot follow them.
  const clickable = q('[routerlink], [to], [data-sveltekit-preload-data], [onclick], [role="link"]')
    .filter((el) => el !== doc.documentElement && el !== body)
    .filter((el) => !(el.tagName === 'A' && el.hasAttribute('href')) && el.tagName !== 'BUTTON');
  const clickable_non_links = {
    count: clickable.length,
    sample: clickable.slice(0, 10).map((el) => ({
      tag: el.tagName.toLowerCase(),
      hint: ['routerlink', 'to', 'data-sveltekit-preload-data', 'onclick', 'role'].find((n) => el.hasAttribute(n)) || null,
      text: clean(el.innerText || el.textContent).slice(0, 80),
    })),
  };

  // -- images ----------------------------------------------------------------
  const images = q('img').filter((i) => !inForeign(i)).map((i) => {
    const src = i.getAttribute('src') || '';
    const alt = i.hasAttribute('alt') ? i.getAttribute('alt') : null;
    const lazy = ['data-src', 'data-lazy-src', 'data-original', 'data-srcset', 'data-lazy']
      .map((n) => i.getAttribute(n)).find(Boolean) || null;
    return { src, resolved: i.currentSrc || (src ? (toUrl(src) || {}).href || null : null), alt,
      alt_empty: alt !== null && !alt.trim(), width: i.getAttribute('width'), height: i.getAttribute('height'),
      loading: i.getAttribute('loading'), lazy_attr: lazy };
  });
  const images_without_alt = images.filter((i) => i.alt === null).length;

  // CSS background images: stylesheet rules (same-origin only) and inline styles, no getComputedStyle.
  const bgElements = new Set(q('[style*="url("]'));
  const collectRules = (rules) => {
    for (const rule of Array.from(rules || [])) {
      if (rule.cssRules) collectRules(rule.cssRules);
      const style = rule.style;
      if (!style || !rule.selectorText) continue;
      if (/url\(/i.test(style.backgroundImage || '') || /url\(/i.test(style.background || '')) {
        try {
          q(rule.selectorText).forEach((el) => bgElements.add(el));
        } catch (e) { /* selector not supported by querySelectorAll */ }
      }
    }
  };
  for (const sheet of Array.from(doc.styleSheets || [])) {
    try {
      collectRules(sheet.cssRules);
    } catch (e) { /* cross-origin stylesheet: rules not readable */ }
  }
  const css_background_images = {
    count: bgElements.size,
    sample: Array.from(bgElements).slice(0, 10).map((el) => el.tagName.toLowerCase() +
      (el.id ? '#' + el.id : '') + (el.classList && el.classList.length ? '.' + Array.from(el.classList).join('.') : '')),
  };

  // -- structured data -------------------------------------------------------------
  const jsonld = [];
  const jsonld_errors = [];
  const typesFound = [];
  const walk = (n) => {
    if (Array.isArray(n)) return n.forEach(walk);
    if (n && typeof n === 'object') {
      for (const t of [].concat(n['@type'] || [])) {
        if (typeof t === 'string' && t && !typesFound.includes(t)) typesFound.push(t);
      }
      for (const [k, v] of Object.entries(n)) if (k !== '@type') walk(v);
    }
    return undefined;
  };
  q('script[type]').filter((s) => s.type.toLowerCase().includes('ld+json')).forEach((s, index) => {
    let raw = String(s.textContent || '').trim();
    let wrapped = false;
    const stripped = raw.replace(/^(<!--|(\/\/\s*)?<!\[CDATA\[)/, '').replace(/(-->|(\/\/\s*)?\]\]>)\s*$/, '').trim();
    if (stripped !== raw) { raw = stripped; wrapped = true; }
    if (!raw) { jsonld_errors.push({ index, error: 'empty JSON-LD block', recovered: false }); return; }
    try {
      const data = JSON.parse(raw);
      jsonld.push(data);
      walk(data);
      if (wrapped) jsonld_errors.push({ index, error: 'wrapped in an HTML comment or CDATA section', recovered: true });
    } catch (e) {
      try {
        const relaxed = raw.replace(/[\u0000-\u001f]+/g, ' ').replace(/,(\s*[}\]])/g, '$1');
        const data = JSON.parse(relaxed);
        jsonld.push(data);
        walk(data);
        jsonld_errors.push({ index, error: 'invalid JSON (recovered leniently): ' + String(e.message || e).slice(0, 200), recovered: true });
      } catch (e2) {
        jsonld_errors.push({ index, error: 'invalid JSON: ' + String(e.message || e).slice(0, 200), recovered: false });
      }
    }
  });
  const jsonld_types = typesFound;
  const microdata_present = !!doc.querySelector('[itemscope], [itemtype]');
  const rdfa_present = !!doc.querySelector('[vocab], [typeof]');

  // -- text --------------------------------------------------------------------
  const visible_text = clean(body ? body.innerText : '');
  const outerNonMain = body ? q(NON_MAIN, body).filter((el) => !el.parentElement || !el.parentElement.closest(NON_MAIN)) : [];
  const nonMainChars = outerNonMain.reduce((sum, el) => sum + clean(el.innerText).length, 0);
  const main_text_chars = Math.max(visible_text.length - nonMainChars, 0);

  // Hidden text: getComputedStyle only on candidate containers (hidden attributes or typical class names).
  const hiddenCandidates = body ? q('[hidden], [aria-hidden="true"], [style*="display:none"], [style*="display: none"], ' +
    '[class*="hidden"], [class*="collapse"], [class*="accordion"], [class*="tab-pane"], [class*="sr-only"]', body) : [];
  const hidden_text_containers = [];
  for (const el of hiddenCandidates.slice(0, 300)) {
    const chars = clean(el.textContent).length;
    if (chars < 100) continue;
    const cs = getComputedStyle(el);
    const reason = el.hidden ? 'hidden attribute' : cs.display === 'none' ? 'display:none'
      : cs.visibility === 'hidden' ? 'visibility:hidden' : Number(cs.opacity) === 0 ? 'opacity:0' : null;
    if (reason) {
      hidden_text_containers.push({ tag: el.tagName.toLowerCase(), id: el.id || null, chars, reason });
    }
  }

  // -- indexability (DOM only: HTTP status and X-Robots-Tag are not visible here) --------
  const reasons = [];
  for (const name of ['robots', 'googlebot']) {
    for (const v of robots_meta[name] || []) {
      const directives = v.toLowerCase().split(',').map((d) => d.trim());
      if (directives.includes('noindex') || directives.includes('none')) reasons.push('noindex in <meta name="' + name + '">');
    }
  }
  const indexable = { value: reasons.length === 0, reasons };

  return {
    url: pageUrl,
    final_url: pageUrl,
    title,
    meta_description,
    robots_meta,
    x_robots_tag: null,
    indexable,
    canonical,
    hreflang,
    hreflang_issues,
    lang,
    viewport,
    og,
    twitter,
    h1,
    headings,
    heading_skips,
    internal_links,
    external_links,
    other_links,
    anchors_without_href,
    images,
    images_without_alt,
    documents,
    jsonld,
    jsonld_errors,
    jsonld_types,
    microdata_present,
    rdfa_present,
    visible_text,
    visible_text_chars: visible_text.length,
    main_text_chars,
    spa_shell_suspect: null,
    head_invalid_tags: null,
    base_href,
    clickable_non_links,
    css_background_images,
    hash_routing_links: Array.from(hashRouting).slice(0, 50),
    hidden_text_containers,
  };
}
