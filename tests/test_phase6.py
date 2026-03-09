"""
Phase 6 — About Section tests.

Covers:
  - Route availability for all 4 about pages (200 OK)
  - 404 for unknown about slugs
  - Page structure (breadcrumb, H1, sections, key content)
  - SEO meta tags (description, canonical, OG)
  - Navigation: navbar + footer links wired to correct routes
  - Regression: phase 4 + 5 routes still return 200
"""

import pytest
from app import app


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def get_html(client, path):
    return client.get(path).data.decode()


# ---------------------------------------------------------------------------
# 1. Route tests
# ---------------------------------------------------------------------------

class TestRoutes:
    def test_who_we_are_returns_200(self, client):
        assert client.get('/about/who-we-are').status_code == 200

    def test_vision_mission_returns_200(self, client):
        assert client.get('/about/vision-mission').status_code == 200

    def test_management_returns_200(self, client):
        assert client.get('/about/management').status_code == 200

    def test_csr_returns_200(self, client):
        assert client.get('/about/csr').status_code == 200

    def test_unknown_about_route_returns_404(self, client):
        assert client.get('/about/does-not-exist').status_code == 404

    def test_about_root_returns_404(self, client):
        r = client.get('/about/')
        assert r.status_code in (301, 302, 404)

    # Regression — previous phases still work
    def test_homepage_still_200(self, client):
        assert client.get('/').status_code == 200

    def test_products_still_200(self, client):
        assert client.get('/products').status_code == 200

    def test_product_detail_still_200(self, client):
        assert client.get('/products/dry-extracts').status_code == 200


# ---------------------------------------------------------------------------
# 2. Who We Are — page structure
# ---------------------------------------------------------------------------

class TestWhoWeAre:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/about/who-we-are')

    def test_page_title(self, html):
        assert 'Who We Are' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Built' in html  # "Built Slow. Built Right."

    def test_breadcrumb_home(self, html):
        assert 'href="/"' in html
        assert 'Home' in html

    def test_breadcrumb_current_page(self, html):
        assert 'aria-current="page"' in html
        assert 'Who We Are' in html

    def test_founded_year_present(self, html):
        assert '1996' in html

    def test_timeline_section_present(self, html):
        assert 'Three Decades' in html or 'Journey' in html

    def test_all_10_milestones_present(self, html):
        years = ['1996', '2001', '2004', '2008', '2012', '2016', '2018', '2021', '2024', '2025']
        for year in years:
            assert year in html, f'Timeline milestone year {year} missing'

    def test_key_strengths_section(self, html):
        assert 'Sourcing Discipline' in html

    def test_cta_strip_present(self, html):
        assert 'Ready to Work with Us' in html or 'Contact Us' in html

    def test_whatsapp_float_button(self, html):
        assert 'fixed bottom-6 right-5' in html

    def test_no_unresolved_jinja_tags(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 3. Vision & Mission — page structure
# ---------------------------------------------------------------------------

class TestVisionMission:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/about/vision-mission')

    def test_page_title(self, html):
        assert 'Vision' in html
        assert 'Mission' in html
        assert 'Vaible Herbal' in html

    def test_h1_manifesto(self, html):
        assert '<h1' in html
        assert 'Quality' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'aria-current="page"' in html

    def test_vision_section_present(self, html):
        assert 'Vision' in html
        assert 'Trusted' in html or 'trusted' in html

    def test_quality_system_loop_present(self, html):
        assert 'Quality System' in html
        assert 'Sourcing' in html
        assert 'Process Control' in html
        assert 'Analytical Verification' in html
        assert 'Release' in html

    def test_4_quality_steps_numbered(self, html):
        for step in ['Step 01', 'Step 02', 'Step 03', 'Step 04']:
            assert step in html, f'{step} missing from quality system loop'

    def test_mission_section_present(self, html):
        assert 'Mission' in html
        assert 'Supply Ingredients' in html

    def test_4_mission_articles(self, html):
        missions = [
            'Supply Ingredients that Perform',
            'Speak the Language',
            'Long-Term Supply',
            'Make Indian Herbal',
        ]
        for m in missions:
            assert m in html, f'Mission item missing: {m}'

    def test_operating_principles_present(self, html):
        assert 'Operating Principles' in html
        assert 'Specification First' in html
        assert 'Traceability Always' in html

    def test_closing_quote(self, html):
        assert 'Quality is not a claim' in html

    def test_whatsapp_float_button(self, html):
        assert 'fixed bottom-6 right-5' in html

    def test_no_unresolved_jinja_tags(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 4. Management — page structure
# ---------------------------------------------------------------------------

class TestManagement:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/about/management')

    def test_page_title(self, html):
        assert 'Management' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Domain Expertise' in html or 'Expertise' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'aria-current="page"' in html

    def test_expertise_areas_present(self, html):
        assert 'Botanical Sourcing' in html
        assert 'Manufacturing Operations' in html
        assert 'Quality' in html

    def test_commitment_section(self, html):
        assert 'Management Accessible' in html or 'Accessible' in html

    def test_no_unresolved_jinja_tags(self, html):
        assert '{{' not in html
        assert '{%' not in html

    def test_whatsapp_float_button(self, html):
        assert 'fixed bottom-6 right-5' in html


# ---------------------------------------------------------------------------
# 5. CSR — page structure
# ---------------------------------------------------------------------------

class TestCSR:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/about/csr')

    def test_page_title(self, html):
        assert 'CSR' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Responsibility' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'aria-current="page"' in html

    def test_responsible_sourcing_present(self, html):
        assert 'Responsible Sourcing' in html

    def test_farmer_community_present(self, html):
        assert 'Farmer' in html or 'Community' in html

    def test_environmental_stewardship_present(self, html):
        assert 'Environmental' in html

    def test_ethical_supply_chain_present(self, html):
        assert 'Ethical Supply Chain' in html

    def test_4_csr_pillars_present(self, html):
        pillars = ['Responsible Sourcing', 'Community', 'Environmental', 'Ethical']
        for p in pillars:
            assert p in html, f'CSR pillar missing: {p}'

    def test_no_unresolved_jinja_tags(self, html):
        assert '{{' not in html
        assert '{%' not in html

    def test_whatsapp_float_button(self, html):
        assert 'fixed bottom-6 right-5' in html


# ---------------------------------------------------------------------------
# 6. SEO meta tags
# ---------------------------------------------------------------------------

class TestSEO:
    @pytest.mark.parametrize('path', [
        '/about/who-we-are',
        '/about/vision-mission',
        '/about/management',
        '/about/csr',
    ])
    def test_meta_description_present(self, client, path):
        html = get_html(client, path)
        assert 'name="description"' in html

    @pytest.mark.parametrize('path,slug', [
        ('/about/who-we-are', 'who-we-are'),
        ('/about/vision-mission', 'vision-mission'),
        ('/about/management', 'management'),
        ('/about/csr', 'csr'),
    ])
    def test_canonical_contains_slug(self, client, path, slug):
        html = get_html(client, path)
        assert f'/about/{slug}' in html

    @pytest.mark.parametrize('path', [
        '/about/who-we-are',
        '/about/vision-mission',
    ])
    def test_og_tags_present(self, client, path):
        html = get_html(client, path)
        assert 'property="og:title"'       in html
        assert 'property="og:description"' in html
        assert 'property="og:url"'         in html
        assert 'property="og:image"'       in html


# ---------------------------------------------------------------------------
# 7. Navigation — navbar + footer links wired correctly
# ---------------------------------------------------------------------------

class TestNavigation:
    def test_desktop_navbar_who_we_are_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/who-we-are"' in html

    def test_desktop_navbar_vision_mission_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/vision-mission"' in html

    def test_desktop_navbar_management_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/management"' in html

    def test_desktop_navbar_csr_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/csr"' in html

    def test_footer_who_we_are_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/who-we-are"' in html

    def test_footer_vision_mission_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/vision-mission"' in html

    def test_footer_csr_link(self, client):
        html = get_html(client, '/')
        assert 'href="/about/csr"' in html

    def test_who_we_are_breadcrumb_links_home(self, client):
        html = get_html(client, '/about/who-we-are')
        assert 'href="/"' in html

    def test_vision_mission_breadcrumb_links_home(self, client):
        html = get_html(client, '/about/vision-mission')
        assert 'href="/"' in html

    def test_vision_mission_cta_links_to_products(self, client):
        html = get_html(client, '/about/vision-mission')
        assert 'href="/products"' in html
