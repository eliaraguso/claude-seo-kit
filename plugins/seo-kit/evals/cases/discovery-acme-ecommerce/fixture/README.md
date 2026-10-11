# Acme Widgets shop

Online shop of Acme Widgets: durable steel and aluminium widgets for workshops, makerspaces and home DIY. We design the widgets in-house and ship from our warehouse.

## Business

- Sells direct to consumers and to small workshops; about 40 products in 4 categories (widgets, mounts, spare parts, kits).
- Markets: United Kingdom (main market, prices in GBP) and Germany (since 2025, prices in EUR, shipping from the same warehouse).
- The site is English-only today. A German version of the shop (`/de/`) is planned for Q1 2027; German customers currently use the English pages.
- Every widget is tested for 1,000 cycles; spare parts stay available for 10 years. Free returns within 30 days.
- Goal for the next year: more orders from people who search for a specific widget type or a replacement part, not only from people who already know the brand.

## Tech

- Static HTML generated from a product spreadsheet (`site/`), deployed to https://acme-widgets.example on Netlify.
- Search Console: not set up yet. Analytics: none.
- No blog. Product pages only, plus home, about and shipping.

## Decisions

- We do not publish stock levels on the site.
- We do not want city landing pages: we ship nationwide, we have no shops.
