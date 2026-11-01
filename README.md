# MetricNote website

Static product, support and privacy pages for MetricNote. English is available at the root; Russian at `/ru/`. The site uses HTML/CSS, native expandable FAQ sections and system fonts. It has no JavaScript, external dependencies, analytics, cookies or contact forms.

## Structure

- `index.html`, `support/index.html`, `privacy/index.html` — English pages.
- `ru/` — Russian equivalents.
- `assets/site.css` — shared responsive styles.
- `assets/app-icon.png` — the existing MetricNote app icon.
- `scripts/check_site.py` — local links, language, headings and asset checks.

The report on the landing page is an illustration with fictional data, not an app screenshot. A download link will be added when the app is published.

## Local preview

```sh
python3 scripts/check_site.py
python3 -m http.server 8080
```

Open `http://localhost:8080/` or `http://localhost:8080/ru/`.

## GitHub Pages

Publish this directory as a separate public repository, for example `metricnote-site`. In repository settings, choose Pages → Deploy from a branch → main → root. The `.nojekyll` file keeps the static site unchanged. Relative links work under a repository URL as well as a custom domain. No build step, server, account registration or environment variables are needed for the website itself.

Publication, repository creation and domain changes have not been performed. After publication, verify HTTPS, both languages and every page. Then put the real support/privacy addresses into the iOS app's `AboutConfiguration.json` and App Store metadata. Canonical URLs and a sitemap can be added after the final domain is selected.

## Content

Support: `lagutoff45@gmail.com`. Copyright owner: Viacheslav Lagutov / Лагутов Вячеслав. Privacy text follows the iOS repository's `AboutPrivacy.json`; keep app and public policy versions aligned. The website includes a separate hosting disclosure. Keep the release status accurate and replace the release notice with the real App Store link after publication.

## Validation

Run `python3 scripts/check_site.py` after changes. Check the home, support and privacy pages in both languages on narrow and wide screens. Verify keyboard navigation, visible focus and native FAQ expansion. Do not add analytics or external services without updating the privacy information.
