# Solvinter.org

Current Astro preview: **astro/**. This version contains Swedish and English pages, the winter-sun banner, About and contact, Eira, MetabolismX, Clinical AI Evaluation, Solvinter Observatory, and the photographer’s complete Ghana selection.

## Run locally

```sh
cd astro
npm ci
ASTRO_TELEMETRY_DISABLED=1 npm run dev
```

To build: `ASTRO_TELEMETRY_DISABLED=1 npm run build`. The static output is `astro/dist/`. To inspect the build: `npm run preview`.

After editing Swedish content or presentation, regenerate English pages with `python3 tools/generate_english.py` before building. English translations are maintained in that script.

## Source and history

The HTML prototype in the repository root and its assets are preserved. The Astro version is saved on the `astro-preview-2026-11-05` branch. No deployment workflow is added by this change. Publishing this version remains a separate action.

Original image archives, private inventory, thumbnails, and curation decisions are excluded. The public image files are the display assets used by the reviewed website. Do not upload the complete original archive.

## Presentation decisions

- Preserve all 69 photographs in the photographer’s Ghana selection. Do not substitute or remove photographs without an explicit request.
- Three collection layouts: Visual rhythm, Gallery, Contact sheet.
- Sections and projects have no decorative numbering. Collection 001 remains the collection’s name.
- The homepage winter banner is 200 px high on desktop, 220 px on wide displays and 180 px on mobile. Cropping uses CSS and does not modify originals.
- The preview retains noindex and draft labels pending publication approval.
