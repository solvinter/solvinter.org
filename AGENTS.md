# Solvinter

The current Astro source is in astro/. Preserve the earlier root HTML prototype and history.

Treat a photographer-created collection as an intentional artistic selection. Collection 001 contains all 69 photographs in astro/public/images/ghana/. Do not add, replace, or remove photographs without an explicit user request. Original image archives remain outside this repository.

Regenerate English routes using `python3 tools/generate_english.py` from astro/ after changing the Swedish source, then build with `ASTRO_TELEMETRY_DISABLED=1 npm run build`.

Do not deploy or change the site audience without authorization. Never commit private archives, curation decisions, credentials, node_modules, or build output.
