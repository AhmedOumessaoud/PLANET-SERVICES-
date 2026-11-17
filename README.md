# Planet Services

Open index.html, or run `python -m http.server 8080` in this folder.

Buildless HTML5 / CSS3 / vanilla JavaScript. Arabic RTL; poster-inspired mobile design.

## Generated imagery
Built-in ImageGen produced four original assets, integrated as optimized WebP images:
- assets/generated/lounge.webp — illustrative Moroccan sports lounge concept.
- assets/generated/stadium.webp — night stadium, Moroccan flag and football.
- assets/generated/supporter.webp — Moroccan supporter, transparent background.
- assets/generated/football.webp — football cutout, transparent background.

Full-resolution PNG originals are alongside the WebP exports. Exact prompts and generator provenance are in assets/GENERATED-ASSETS.json. These images are illustrative, not real shop photographs. The interior is captioned accordingly. Replace with genuine interior photographs when supplied.

## Official brand logos
assets/brands/ contains original TIFO, CHRONO, MDJS and COTE & SPORT logos downloaded from https://mdjs.ma/jeux/ and LOTO from https://www.loterie.ma/loto/. Exact asset URLs are recorded in assets/brands/SOURCES.json. Existing Planet Services branding and screen captures remain extracted from the user-supplied poster.

## Vector icons
Official Lucide SVGs replace emoji/glyph placeholders for users, armchair, sports TV, lightning, calendar/clock, map pin, menu, close and back-to-top. WhatsApp uses the Bootstrap Icons brand SVG. Assets and required license notices are included in assets/icons/. SVGs are embedded directly, without runtime dependencies or icon-font downloads.

## Maintenance
Edit index.html, style.css and script.js directly. Generator scripts document earlier preparation stages; do not rerun them over the customized page. Google Fonts and the map embed require internet. Contact and directions links use the supplied exact destinations.

## Reference-matched mobile layout
At widths up to 760px, index.html presents .poster-page, a dedicated compact poster composition with local Tajawal fonts and CSS container units. poster.css controls the proportions independently of the desktop design. Headings, descriptions, hours, address and contact details are live HTML. The header branding, interior, supporter, separate service illustrations, pin/map illustration and stadium crowd come from individually extracted user-supplied reference assets. Generated imagery remains available for desktop. The mobile contact address and red CTA open directions; the phone panel calls Mourad; WhatsApp remains in the stadium footer. Gallery images share the existing lightbox.

Chrome mobile full-page visual review completed at 400px width. Result approximately 1432px tall (3.58:1), close to the 2365/665 reference ratio of 3.56:1; prior user screenshot was 3736/480 (7.78:1). Final minor typography adjustments followed visual review. A later interaction check was interrupted when the user minimized Chrome, so lightbox behavior was not re-tested through the UI this turn.


## Client revision — 2026-11-17
Client-supplied KENO logo and four screen captures live in assets/client/. SOURCES.json records their filenames. The duplicate Lmatch Pro attachment is pixel-identical and is used only once. Both mobile and desktop galleries use these new images, preserve the entire frame, and open the full-resolution original on click. The approved slogan is now in both hero layouts. KENO is the sixth service; no unprovided prizes, odds or offers are advertised. Screenshot data is illustrative, not live.
