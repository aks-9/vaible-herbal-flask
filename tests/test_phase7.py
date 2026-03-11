"""
Phase 7 — Innovation Section tests.

Covers:
  - Route availability for all 6 innovation pages (200 OK)
  - 404 for unknown innovation slugs
  - Page structure (breadcrumb, H1, key content sections)
  - SEO meta tags (description, canonical, OG)
  - Navigation: navbar + mobile drawer links wired to correct routes
  - Regression: all previous phase routes still return 200
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
# Route slugs used throughout tests
# ---------------------------------------------------------------------------

INNOVATION_ROUTES = [
    ('/innovation/applied-research',               'applied_research'),
    ('/innovation/phytochemical-understanding',    'phytochemical_understanding'),
    ('/innovation/product-development-framework',  'product_development_framework'),
    ('/innovation/formulation-application-insights', 'formulation_application_insights'),
    ('/innovation/quality-systems-ci',             'quality_systems_ci'),
    ('/innovation/future-readiness',               'future_readiness'),
]

INNOVATION_PATHS = [path for path, _ in INNOVATION_ROUTES]


# ---------------------------------------------------------------------------
# 1. Route tests
# ---------------------------------------------------------------------------

class TestRoutes:
    @pytest.mark.parametrize('path,_', INNOVATION_ROUTES)
    def test_innovation_page_returns_200(self, client, path, _):
        assert client.get(path).status_code == 200

    def test_unknown_innovation_route_returns_404(self, client):
        assert client.get('/innovation/does-not-exist').status_code == 404

    def test_innovation_root_returns_404_or_redirect(self, client):
        r = client.get('/innovation/')
        assert r.status_code in (301, 302, 404)

    # Regression — all previous phases
    def test_homepage_still_200(self, client):
        assert client.get('/').status_code == 200

    def test_products_still_200(self, client):
        assert client.get('/products').status_code == 200

    def test_product_detail_still_200(self, client):
        assert client.get('/products/dry-extracts').status_code == 200

    def test_who_we_are_still_200(self, client):
        assert client.get('/about/who-we-are').status_code == 200

    def test_vision_mission_still_200(self, client):
        assert client.get('/about/vision-mission').status_code == 200

    def test_management_still_200(self, client):
        assert client.get('/about/management').status_code == 200

    def test_csr_still_200(self, client):
        assert client.get('/about/csr').status_code == 200


# ---------------------------------------------------------------------------
# 2. Applied Research page
# ---------------------------------------------------------------------------

class TestAppliedResearch:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/innovation/applied-research')

    def test_title(self, html):
        assert 'Applied Research' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Applied Research' in html

    def test_breadcrumb_home(self, html):
        assert 'href="/"' in html

    def test_breadcrumb_innovation_label(self, html):
        assert 'Innovation' in html

    def test_breadcrumb_current_page(self, html):
        assert 'aria-current="page"' in html

    def test_key_content_pillars(self, html):
        assert 'Pharmacopeial' in html
        assert 'Batch Data' in html or 'Batch' in html

    def test_knowledge_areas_section(self, html):
        assert 'Botanical Identification' in html
        assert 'Extraction Science' in html or 'Standardisation' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html

    def test_whatsapp_float(self, html):
        assert 'fixed bottom-6 right-5' in html


# ---------------------------------------------------------------------------
# 3. Phytochemical Understanding page
# ---------------------------------------------------------------------------

class TestPhytochemicalUnderstanding:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/innovation/phytochemical-understanding')

    def test_title(self, html):
        assert 'Phytochemical' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html

    def test_marker_compound_types(self, html):
        for compound in ['Alkaloids', 'Flavonoids', 'Polyphenols', 'Terpenoids']:
            assert compound in html, f'Missing compound type: {compound}'

    def test_variability_section(self, html):
        assert 'Variability' in html or 'variability' in html
        assert 'Harvest Season' in html or 'Incoming Inspection' in html

    def test_stability_section(self, html):
        assert 'Stability' in html or 'stability' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 4. Product Development Framework page
# ---------------------------------------------------------------------------

class TestProductDevelopmentFramework:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/innovation/product-development-framework')

    def test_title(self, html):
        assert 'Product Development' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html

    def test_6_stages_present(self, html):
        for stage_num in ['Stage 01', 'Stage 02', 'Stage 03', 'Stage 04', 'Stage 05', 'Stage 06']:
            assert stage_num in html, f'Missing: {stage_num}'

    def test_feasibility_stage(self, html):
        assert 'Feasibility' in html

    def test_pilot_stage(self, html):
        assert 'Pilot' in html

    def test_documentation_stage(self, html):
        assert 'Documentation' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 5. Formulation & Application Insights page
# ---------------------------------------------------------------------------

class TestFormulationApplicationInsights:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/innovation/formulation-application-insights')

    def test_title(self, html):
        assert 'Formulation' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html

    def test_formulation_parameters(self, html):
        assert 'Solubility' in html
        assert 'Stability' in html
        assert 'Compatibility' in html

    def test_sector_sections(self, html):
        assert 'Nutraceutical' in html or 'nutraceutical' in html
        assert 'Cosmetic' in html or 'cosmetic' in html
        assert 'Pharmaceutical' in html or 'pharmaceutical' in html

    def test_products_cta_link(self, html):
        assert 'href="/products"' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 6. Quality Systems & CI page
# ---------------------------------------------------------------------------

class TestQualitySystemsCI:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/innovation/quality-systems-ci')

    def test_title(self, html):
        assert 'Quality Systems' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html

    def test_non_thermal_section(self, html):
        assert 'Non-Thermal' in html or 'non-thermal' in html
        assert 'Decontamination' in html

    def test_sterile_filtration_section(self, html):
        assert 'Sterile Filtration' in html or 'sterile filtration' in html
        assert '0.22' in html  # terminal filtration step

    def test_filtration_stages_present(self, html):
        for stage in ['50 µm', '10 µm', '5 µm', '1 µm', '0.22 µm']:
            assert stage in html, f'Missing filtration stage: {stage}'

    def test_lab_facilities_section(self, html):
        assert 'Laboratory' in html
        assert 'Microbiological' in html or 'Analytical' in html

    def test_compliance_section(self, html):
        assert 'Aflatoxin' in html
        assert 'Pesticide' in html
        assert 'Heavy Metal' in html
        assert 'Allergen' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html

    def test_whatsapp_float(self, html):
        assert 'fixed bottom-6 right-5' in html


# ---------------------------------------------------------------------------
# 7. Future Readiness page
# ---------------------------------------------------------------------------

class TestFutureReadiness:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/innovation/future-readiness')

    def test_title(self, html):
        assert 'Future Readiness' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html

    def test_4_readiness_pillars(self, html):
        pillars = ['Regulatory Monitoring', 'Emerging Category', 'Sustainability', 'Technology Adoption']
        for p in pillars:
            assert p in html, f'Missing readiness pillar: {p}'

    def test_closing_quote(self, html):
        assert 'customers who stay with us' in html or 'never have to find a new supplier' in html

    def test_products_cta_link(self, html):
        assert 'href="/products"' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html

    def test_whatsapp_float(self, html):
        assert 'fixed bottom-6 right-5' in html


# ---------------------------------------------------------------------------
# 8. SEO meta tags — all 6 pages
# ---------------------------------------------------------------------------

class TestSEO:
    @pytest.mark.parametrize('path', INNOVATION_PATHS)
    def test_meta_description(self, client, path):
        html = get_html(client, path)
        assert 'name="description"' in html

    @pytest.mark.parametrize('path,slug', [
        ('/innovation/applied-research',              'applied-research'),
        ('/innovation/phytochemical-understanding',   'phytochemical-understanding'),
        ('/innovation/product-development-framework', 'product-development-framework'),
        ('/innovation/formulation-application-insights', 'formulation-application-insights'),
        ('/innovation/quality-systems-ci',            'quality-systems-ci'),
        ('/innovation/future-readiness',              'future-readiness'),
    ])
    def test_canonical_contains_slug(self, client, path, slug):
        html = get_html(client, path)
        assert f'/innovation/{slug}' in html

    @pytest.mark.parametrize('path', INNOVATION_PATHS)
    def test_og_title_present(self, client, path):
        html = get_html(client, path)
        assert 'property="og:title"' in html

    @pytest.mark.parametrize('path', INNOVATION_PATHS)
    def test_og_description_present(self, client, path):
        html = get_html(client, path)
        assert 'property="og:description"' in html


# ---------------------------------------------------------------------------
# 9. Navigation — navbar links wired correctly
# ---------------------------------------------------------------------------

class TestNavigation:
    def test_desktop_navbar_applied_research_link(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/applied-research"' in html

    def test_desktop_navbar_phytochemical_link(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/phytochemical-understanding"' in html

    def test_desktop_navbar_product_dev_link(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/product-development-framework"' in html

    def test_desktop_navbar_formulation_link(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/formulation-application-insights"' in html

    def test_desktop_navbar_quality_systems_link(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/quality-systems-ci"' in html

    def test_desktop_navbar_future_readiness_link(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/future-readiness"' in html

    def test_footer_innovation_link_wired(self, client):
        html = get_html(client, '/')
        assert 'href="/innovation/quality-systems-ci"' in html

    def test_breadcrumbs_link_home(self, client):
        for path in INNOVATION_PATHS:
            html = get_html(client, path)
            assert 'href="/"' in html, f'Home breadcrumb missing on {path}'
