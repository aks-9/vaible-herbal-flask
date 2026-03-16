"""
Phase 9 — Contact + Forms tests.

Covers:
  - Route availability: /contact returns 200
  - 404 for unknown routes
  - Page structure: breadcrumb, H1, form, quick contact, locations, map
  - Form fields: name, company, email, phone, interest, purpose, message
  - SEO meta tags: description, canonical, OG
  - Navigation: navbar + footer contact links wired to /contact
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
# 1. Route tests
# ---------------------------------------------------------------------------

class TestRoutes:
    def test_contact_returns_200(self, client):
        assert client.get('/contact').status_code == 200

    def test_contact_unknown_slug_404(self, client):
        assert client.get('/contact/nonexistent').status_code == 404


# ---------------------------------------------------------------------------
# 2. Page structure
# ---------------------------------------------------------------------------

class TestPageStructure:
    def test_h1_contains_contact(self, client):
        html = get_html(client, '/contact')
        assert 'Contact Vaible Herbal' in html

    def test_breadcrumb_present(self, client):
        html = get_html(client, '/contact')
        assert 'Breadcrumb' in html
        assert 'Contact Us' in html

    def test_breadcrumb_home_link(self, client):
        html = get_html(client, '/contact')
        assert 'href="/"' in html or 'url_for' in html or 'Home' in html

    def test_contact_form_present(self, client):
        html = get_html(client, '/contact')
        assert 'contactForm' in html

    def test_quick_contact_section(self, client):
        html = get_html(client, '/contact')
        assert 'Quick Contact' in html

    def test_locations_section(self, client):
        html = get_html(client, '/contact')
        assert 'Offices' in html or 'Facilities' in html or 'locations' in html.lower()

    def test_map_section(self, client):
        html = get_html(client, '/contact')
        assert 'loadMap' in html or 'Load Map' in html

    def test_whatsapp_float(self, client):
        html = get_html(client, '/contact')
        assert 'wa.me' in html

    def test_page_hero_chips_present(self, client):
        html = get_html(client, '/contact')
        assert 'B2B Manufacturing Partner' in html

    def test_response_policy_card(self, client):
        html = get_html(client, '/contact')
        assert 'Response Policy' in html


# ---------------------------------------------------------------------------
# 3. Contact form fields
# ---------------------------------------------------------------------------

class TestContactFormFields:
    def test_name_field(self, client):
        html = get_html(client, '/contact')
        assert 'contactName' in html

    def test_company_field(self, client):
        html = get_html(client, '/contact')
        assert 'contactCompany' in html

    def test_email_field(self, client):
        html = get_html(client, '/contact')
        assert 'contactEmail' in html

    def test_phone_field(self, client):
        html = get_html(client, '/contact')
        assert 'contactPhone' in html

    def test_interest_select(self, client):
        html = get_html(client, '/contact')
        assert 'contactInterest' in html
        assert 'Herbal Extracts' in html
        assert 'Essential Oils' in html

    def test_purpose_select(self, client):
        html = get_html(client, '/contact')
        assert 'contactPurpose' in html
        assert 'Quotation' in html
        assert 'Sample Request' in html

    def test_message_textarea(self, client):
        html = get_html(client, '/contact')
        assert 'contactMessage' in html

    def test_submit_button(self, client):
        html = get_html(client, '/contact')
        assert 'Submit Message' in html

    def test_toast_element(self, client):
        html = get_html(client, '/contact')
        assert 'contactToast' in html

    def test_form_submit_js_handler(self, client):
        html = get_html(client, '/contact')
        assert 'submitContactForm' in html

    def test_required_fields_marked(self, client):
        html = get_html(client, '/contact')
        assert 'required' in html


# ---------------------------------------------------------------------------
# 4. Quick contact details
# ---------------------------------------------------------------------------

class TestQuickContactDetails:
    def test_email_address(self, client):
        html = get_html(client, '/contact')
        assert 'Sales@VaibleHerbal.com' in html

    def test_phone_number(self, client):
        html = get_html(client, '/contact')
        assert '99111 54497' in html or '9911154497' in html

    def test_business_hours(self, client):
        html = get_html(client, '/contact')
        assert 'Mon' in html and 'IST' in html

    def test_whatsapp_link_in_sidebar(self, client):
        html = get_html(client, '/contact')
        assert 'Chat on WhatsApp' in html


# ---------------------------------------------------------------------------
# 5. Locations
# ---------------------------------------------------------------------------

class TestLocations:
    def test_okhla_office(self, client):
        html = get_html(client, '/contact')
        assert 'Okhla' in html

    def test_raj_nagar_office(self, client):
        html = get_html(client, '/contact')
        assert 'Raj Nagar' in html

    def test_nahan_facility(self, client):
        html = get_html(client, '/contact')
        assert 'Nahan' in html

    def test_badarpur_warehouse(self, client):
        html = get_html(client, '/contact')
        assert 'Badarpur' in html


# ---------------------------------------------------------------------------
# 6. SEO meta tags
# ---------------------------------------------------------------------------

class TestSEO:
    def test_meta_description(self, client):
        html = get_html(client, '/contact')
        assert 'meta name="description"' in html
        assert 'herbal' in html.lower()

    def test_canonical_tag(self, client):
        html = get_html(client, '/contact')
        assert 'rel="canonical"' in html
        assert '/contact' in html

    def test_og_title(self, client):
        html = get_html(client, '/contact')
        assert 'og:title' in html
        assert 'Contact' in html

    def test_og_description(self, client):
        html = get_html(client, '/contact')
        assert 'og:description' in html

    def test_og_url(self, client):
        html = get_html(client, '/contact')
        assert 'og:url' in html

    def test_og_image(self, client):
        html = get_html(client, '/contact')
        assert 'og:image' in html

    def test_og_site_name(self, client):
        html = get_html(client, '/contact')
        assert 'Vaible Herbal' in html

    def test_page_title(self, client):
        html = get_html(client, '/contact')
        assert '<title>' in html
        assert 'Contact' in html


# ---------------------------------------------------------------------------
# 7. Navigation wiring
# ---------------------------------------------------------------------------

class TestNavigation:
    def test_navbar_contact_link_wired(self, client):
        # navbar CTA "Contact Us" button should link to /contact on any page
        html = get_html(client, '/')
        assert '/contact' in html

    def test_footer_contact_link_wired(self, client):
        html = get_html(client, '/contact')
        assert '/contact' in html

    def test_contact_page_links_back_to_home(self, client):
        html = get_html(client, '/contact')
        assert 'href="/"' in html


# ---------------------------------------------------------------------------
# 8. Regression — all previous phase routes still 200
# ---------------------------------------------------------------------------

REGRESSION_ROUTES = [
    '/',
    '/products',
    '/products/dry-extracts',
    '/about/who-we-are',
    '/about/vision-mission',
    '/about/management',
    '/about/csr',
    '/innovation/applied-research',
    '/innovation/phytochemical-understanding',
    '/innovation/product-development-framework',
    '/innovation/formulation-application-insights',
    '/innovation/quality-systems-ci',
    '/innovation/future-readiness',
    '/resources/news-blogs',
    '/resources/webinar',
    '/resources/events',
    '/resources/career',
    '/resources/brochure',
    '/contact',
]


class TestRegression:
    @pytest.mark.parametrize('path', REGRESSION_ROUTES)
    def test_route_returns_200(self, client, path):
        assert client.get(path).status_code == 200

    def test_404_for_unknown(self, client):
        assert client.get('/does-not-exist-xyz').status_code == 404
