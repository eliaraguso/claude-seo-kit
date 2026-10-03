// Estrae dal DOM renderizzato (dopo JavaScript) gli stessi campi di seo_fetch.py,
// per confrontare ciò che vede un browser con l'HTML grezzo del server.
// Uso: incollare come funzione in evaluate_script (Chrome DevTools MCP) o nella console.
() => {
  const q = (s) => Array.from(document.querySelectorAll(s));
  const meta = (n) => q(`meta[name="${n}"], meta[property="${n}"]`).map((m) => m.content);
  const host = location.host;
  const links = q('a');
  const internal = new Set();
  let external = 0;
  for (const a of links) {
    const href = a.getAttribute('href');
    if (!href || /^(#|mailto:|tel:|javascript:)/.test(href)) continue;
    const u = new URL(href, location.href);
    if (u.host === host) internal.add(u.origin + u.pathname + u.search);
    else external++;
  }
  const jsonld = q('script[type="application/ld+json"]').map((s) => {
    try {
      const d = JSON.parse(s.textContent);
      const types = [];
      const walk = (n) => {
        if (Array.isArray(n)) return n.forEach(walk);
        if (n && typeof n === 'object') {
          if (n['@type']) types.push(...[].concat(n['@type']));
          ['@graph', 'mainEntity', 'author', 'publisher', 'itemListElement'].forEach((k) => n[k] && walk(n[k]));
        }
      };
      walk(d);
      return { ok: true, types };
    } catch (e) {
      return { ok: false, error: String(e).slice(0, 120) };
    }
  });
  const headings = {};
  for (const h of q('h1,h2,h3,h4,h5,h6')) headings[h.tagName.toLowerCase()] = (headings[h.tagName.toLowerCase()] || 0) + 1;
  return {
    url: location.href,
    lang: document.documentElement.lang || null,
    title: document.title,
    meta_description: meta('description'),
    robots_meta: [...meta('robots').map((c) => 'robots: ' + c), ...meta('googlebot').map((c) => 'googlebot: ' + c)],
    canonical: q('link[rel="canonical"]').map((l) => l.getAttribute('href')),
    hreflang: q('link[rel="alternate"][hreflang]').map((l) => `${l.hreflang} -> ${l.getAttribute('href')}`),
    h1: q('h1').map((h) => h.innerText.trim()),
    headings,
    og: Object.fromEntries(q('meta[property^="og:"]').map((m) => [m.getAttribute('property'), m.content])),
    jsonld,
    links_internal: internal.size,
    links_external: external,
    a_without_href: links.filter((a) => !a.getAttribute('href')).length,
    clickable_non_links: q('[routerlink]:not(a), [onclick]:not(a):not(button), div[role="link"], span[role="link"]').length,
    img: q('img').length,
    img_no_alt: q('img:not([alt])').length,
    css_background_images: q('*').filter((e) => getComputedStyle(e).backgroundImage.startsWith('url(')).length,
    visible_text_chars: document.body.innerText.replace(/\s+/g, ' ').trim().length,
    location_hash_routing: /^#\//.test(location.hash),
  };
}
