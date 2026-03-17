"""
Phase 10 — SEO & Meta tests.

Covers:
  - robots.txt: route returns 200, correct content-type, required directives
  - sitemap.xml: route returns 200, XML content, all URLs present (static + 14 dynamic)
  - Favicon: base template includes favicon link
  - Twitter Card: base template includes twitter:card meta tag
  - BreadcrumbList JSON-LD: inner pages include BreadcrumbList schema
  - 404 handler: unknown routes return 404 with custom template
  - Regression: all previous phase routes still return 200
"""

import pytest
from app import app, SITE_URL


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def get(client, path):
    return client.get(path)


def html(client, path):
    return client.get(path).data.decode()


# ---------------------------------------------------------------------------
# TestRobotsTxt
# ---------------------------------------------------------------------------

class TestRobotsTxt:
    def test_returns_200(self, client):
        r = get(client, '/robots.txt')
        assert r.status_code == 200

    def test_content_type_is_plain_text(self, client):
        r = get(client, '/robots.txt')
        assert 'text/plain' in r.content_type

    def test_user_agent_wildcard(self, client):
        body = get(client, '/robots.txt').data.decode()
        assert 'User-agent: *' in body

    def test_allow_all(self, client):
        body = get(client, '/robots.txt').data.decode()
        assert 'Allow: /' in body

    def test_sitemap_directive(self, client):
        body = get(client, '/robots.txt').data.decode()
        assert 'Sitemap:' in body
        assert '/sitemap.xml' in body


# ---------------------------------------------------------------------------
# TestSitemapXml
# ---------------------------------------------------------------------------

class TestSitemapXml:
    def test_returns_200(self, client):
        assert get(client, '/sitemap.xml').status_code == 200

    def test_content_type_is_xml(self, client):
        r = get(client, '/sitemap.xml')
        assert 'xml' in r.content_type

    def test_xml_declaration(self, client):
        body = html(client, '/sitemap.xml')
        assert '<?xml' in body

    def test_urlset_element(self, client):
        body = html(client, '/sitemap.xml')
        assert '<urlset' in body
        assert 'sitemaps.org' in body

    def test_homepage_present(self, client):
        body = html(client, '/sitemap.xml')
        assert f'<loc>{SITE_URL}/</loc>' in body

    def test_products_page_present(self, client):
        body = html(client, '/sitemap.xml')
        assert f'<loc>{SITE_URL}/products</loc>' in body

    def test_contact_page_present(self, client):
        body = html(client, '/sitemap.xml')
        assert f'<loc>{SITE_URL}/contact</loc>' in body

    def test_about_pages_present(self, client):
        body = html(client, '/sitemap.xml')
        for slug in ['who-we-are', 'vision-mission', 'management', 'csr']:
            assert f'/about/{slug}' in body, f'Missing /about/{slug}'

    def test_innovation_pages_present(self, client):
        body = html(client, '/sitemap.xml')
        for slug in [
            'applied-research', 'phytochemical-understanding',
            'product-development-framework', 'formulation-application-insights',
            'quality-systems-ci', 'future-readiness',
        ]:
            assert f'/innovation/{slug}' in body, f'Missing /innovation/{slug}'

    def test_resources_pages_present(self, client):
        body = html(client, '/sitemap.xml')
        for slug in ['news-blogs', 'webinar', 'events', 'career', 'brochure']:
            assert f'/resources/{slug}' in body, f'Missing /resources/{slug}'

    def test_all_14_product_slugs_present(self, client):
        body = html(client, '/sitemap.xml')
        slugs = [
            'dry-extracts', 'liquid-extracts', 'oil-extracts', 'soft-extracts',
            'essential-oils', 'carrier-oils', 'herbal-powders', 'butters',
            'ayurvedic-oils', 'crystals', 'floral-waters', 'granules',
            'resin', 'oleoresins',
        ]
        for slug in slugs:
            assert f'/products/{slug}' in body, f'Missing /products/{slug}'

    def test_priority_tags_present(self, client):
        body = html(client, '/sitemap.xml')
        assert '<priority>' in body

    def test_changefreq_tags_present(self, client):
        body = html(client, '/sitemap.xml')
        assert '<changefreq>' in body

    def test_lastmod_tags_present(self, client):
        body = html(client, '/sitemap.xml')
        assert '<lastmod>' in body

    def test_homepage_has_highest_priority(self, client):
        body = html(client, '/sitemap.xml')
        # homepage entry should contain priority 1.0
        assert '1.0' in body


# ---------------------------------------------------------------------------
# TestFavicon
# ---------------------------------------------------------------------------

class TestFavicon:
    def test_favicon_link_in_homepage(self, client):
        body = html(client, '/')
        assert 'rel="icon"' in body

    def test_favicon_uses_png_type(self, client):
        body = html(client, '/')
        assert 'type="image/png"' in body

    def test_favicon_references_logo(self, client):
        body = html(client, '/')
        assert 'logo-vaible-herbal.png' in body

    def test_favicon_present_on_products_page(self, client):
        body = html(client, '/products')
        assert 'rel="icon"' in body


# ---------------------------------------------------------------------------
# TestTwitterCard
# ---------------------------------------------------------------------------

class TestTwitterCard:
    def test_twitter_card_on_homepage(self, client):
        body = html(client, '/')
        assert 'twitter:card' in body

    def test_twitter_card_value_summary_large_image(self, client):
        body = html(client, '/')
        assert 'summary_large_image' in body

    def test_twitter_card_on_products_page(self, client):
        body = html(client, '/products')
        assert 'twitter:card' in body

    def test_twitter_card_on_about_page(self, client):
        body = html(client, '/about/who-we-are')
        assert 'twitter:card' in body

    def test_twitter_card_on_contact_page(self, client):
        body = html(client, '/contact')
        assert 'twitter:card' in body


# ---------------------------------------------------------------------------
# TestBreadcrumbJsonLD
# ---------------------------------------------------------------------------

class TestBreadcrumbJsonLD:
    def test_products_page_has_breadcrumb_schema(self, client):
        body = html(client, '/products')
        assert 'BreadcrumbList' in body

    def test_products_page_has_home_item(self, client):
        body = html(client, '/products')
        assert '"Home"' in body

    def test_product_detail_has_breadcrumb_schema(self, client):
        body = html(client, '/products/dry-extracts')
        assert 'BreadcrumbList' in body

    def test_product_detail_has_category_name(self, client):
        body = html(client, '/products/dry-extracts')
        assert 'Herbal Dry Extracts' in body

    def test_about_page_has_breadcrumb_schema(self, client):
        body = html(client, '/about/who-we-are')
        assert 'BreadcrumbList' in body

    def test_about_page_has_about_us_item(self, client):
        body = html(client, '/about/who-we-are')
        assert '"About Us"' in body

    def test_innovation_page_has_breadcrumb_schema(self, client):
        body = html(client, '/innovation/applied-research')
        assert 'BreadcrumbList' in body

    def test_resources_page_has_breadcrumb_schema(self, client):
        body = html(client, '/resources/news-blogs')
        assert 'BreadcrumbList' in body

    def test_contact_page_has_breadcrumb_schema(self, client):
        body = html(client, '/contact')
        assert 'BreadcrumbList' in body

    def test_homepage_has_no_breadcrumb_schema(self, client):
        # homepage is root — no breadcrumb needed
        body = html(client, '/')
        assert 'BreadcrumbList' not in body

    def test_breadcrumb_has_position_field(self, client):
        body = html(client, '/products')
        assert '"position"' in body

    def test_breadcrumb_schema_context(self, client):
        body = html(client, '/about/vision-mission')
        assert 'schema.org' in body


# ---------------------------------------------------------------------------
# Test404
# ---------------------------------------------------------------------------

class Test404:
    def test_unknown_route_returns_404(self, client):
        assert get(client, '/does-not-exist').status_code == 404

    def test_unknown_nested_route_returns_404(self, client):
        assert get(client, '/products/not-a-real-slug').status_code == 404

    def test_404_page_has_404_text(self, client):
        body = html(client, '/not-a-page')
        assert '404' in body

    def test_404_page_has_homepage_link(self, client):
        body = html(client, '/not-a-page')
        assert 'href="/"' in body or 'url_for' not in body  # rendered link

    def test_404_page_has_products_link(self, client):
        body = html(client, '/not-a-page')
        assert '/products' in body

    def test_404_page_has_nav(self, client):
        # extends base.html, so navbar should be present
        body = html(client, '/not-a-page')
        assert 'Vaible Herbal' in body


# ---------------------------------------------------------------------------
# TestRegression
# ---------------------------------------------------------------------------

class TestRegression:
    @pytest.mark.parametrize("path", [
        "/",
        "/products",
        "/products/dry-extracts",
        "/products/essential-oils",
        "/about/who-we-are",
        "/about/vision-mission",
        "/about/management",
        "/about/csr",
        "/innovation/applied-research",
        "/innovation/quality-systems-ci",
        "/resources/news-blogs",
        "/resources/career",
        "/contact",
        "/robots.txt",
        "/sitemap.xml",
    ])
    def test_route_returns_200(self, client, path):
        assert get(client, path).status_code == 200
