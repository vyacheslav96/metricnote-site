"""Validate all pages, language links, local assets and publication readiness."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

class PageParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.language = None
        self.h1_count = 0
        self.external_assets = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'html':
            self.language = values.get('lang')
        if tag == 'h1':
            self.h1_count += 1
        if 'id' in values:
            if not values['id'] not in self.ids:
                raise AssertionError(f"Duplicate ID: {values['id']}")
            self.ids.add(values['id'])
        if tag == 'a' and 'href' in values:
            self.links.append(values['href'])
        if tag in ('img', 'script') and 'src' in values:
            self.links.append(values['src'])
        if tag == 'link' and values.get('rel') in ('stylesheet', 'icon'):
            self.links.append(values['href'])
        if tag in ('script', 'img', 'link'):
            source = values.get('src', values.get('href', ''))
            if urlsplit(source).scheme in ('http', 'https'):
                self.external_assets.append(source)

def main():
    root = Path(__file__).resolve().parents[1]
    pages = {page.resolve(): PageParser() for page in root.rglob('*.html')}
    if not len(pages) == 6:
        raise AssertionError(f'Expected 6 localized pages, found {len(pages)}')
    for page, parser in pages.items():
        parser.feed(page.read_text())
        if not parser.language in ('ru', 'en'):
            raise AssertionError(f'Invalid language: {page}')
        if not parser.h1_count == 1:
            raise AssertionError(f'Expected one H1: {page}')
        if not not parser.external_assets:
            raise AssertionError(f'Unexpected external assets: {parser.external_assets}')
        if not 'lagutoff45@gmail.com' in page.read_text():
            raise AssertionError(f'Missing support contact: {page}')
    links = 0
    for page, parser in pages.items():
        for address in parser.links:
            parsed = urlsplit(address)
            if parsed.scheme in ('https', 'mailto'):
                continue
            if not (not parsed.scheme and (not parsed.netloc)):
                raise AssertionError(f'Unexpected link: {address}')
            if not not parsed.path.startswith('/'):
                raise AssertionError(f'Absolute path breaks project hosting: {address}')
            target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_relative_to(root):
                raise AssertionError(f'Path escapes site: {address}')
            if not target.exists():
                raise AssertionError(f'Missing link target: {page.name} -> {address}')
            if parsed.fragment:
                if not (target in pages and unquote(parsed.fragment) in pages[target].ids):
                    raise AssertionError(f'Missing fragment: {address}')
            links += 1
    print(f'Validated {len(pages)} pages and {links} local links/assets; no remote dependencies.')
if __name__ == '__main__':
    main()
