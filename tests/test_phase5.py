"""
Phase 5 — Product Detail Pages tests.

Covers:
  - Route availability for all 14 category slugs
  - 404 for unknown slugs
  - Page structure (breadcrumb, H1, search bar, filters, modal, CTA strip)
  - SEO meta tags (description, canonical, OG)
  - Products JSON data injected into page for JS consumption
  - Navigation: catalogue cards now link to /products/<slug>
  - data/product_items.py integrity (fields, uniqueness, helpers)
"""

import json
import re
import pytest
from app import app
from data.products import CATEGORIES
from data.product_items import (
    ITEMS, get_items, get_all_industries, get_all_functions
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def detail_html(client, slug):
    return client.get(f'/products/{slug}').data.decode()


# ---------------------------------------------------------------------------
# 1. Route tests
# ---------------------------------------------------------------------------

class TestRoutes:
    def test_all_14_slugs_return_200(self, client):
        for cat in CATEGORIES:
            r = client.get(f'/products/{cat["slug"]}')
            assert r.status_code == 200, (
                f'/products/{cat["slug"]} returned {r.status_code}'
            )

    def test_unknown_slug_returns_404(self, client):
        assert client.get('/products/does-not-exist').status_code == 404

    def test_empty_slug_returns_404(self, client):
        # /products/ with trailing slash is a redirect or 404, not a detail page
        r = client.get('/products/')
        assert r.status_code in (301, 302, 404)

    def test_products_catalogue_still_200(self, client):
        assert client.get('/products').status_code == 200

    def test_homepage_still_200(self, client):
        assert client.get('/').status_code == 200


# ---------------------------------------------------------------------------
# 2. Page structure (spot-check on dry-extracts)
# ---------------------------------------------------------------------------

class TestPageStructure:
    @pytest.fixture
    def html(self, client):
        return detail_html(client, 'dry-extracts')

    def test_page_title_contains_category_name(self, html):
        assert 'Herbal Dry Extracts' in html
        assert 'Vaible Herbal' in html

    def test_h1_contains_category_name(self, html):
        assert '<h1' in html
        assert 'Herbal Dry Extracts' in html

    def test_breadcrumb_home_link(self, html):
        assert 'Home' in html
        assert 'href="/"' in html

    def test_breadcrumb_products_link(self, html):
        assert 'href="/products"' in html

    def test_breadcrumb_current_page(self, html):
        assert 'aria-current="page"' in html

    def test_search_input_present(self, html):
        assert 'id="pdSearch"' in html

    def test_industry_filter_present(self, html):
        assert 'id="pdFilterIndustry"' in html

    def test_function_filter_present(self, html):
        assert 'id="pdFilterFunction"' in html

    def test_sort_select_present(self, html):
        assert 'id="pdSort"' in html

    def test_product_grid_present(self, html):
        assert 'id="pdGrid"' in html

    def test_empty_state_present(self, html):
        assert 'id="pdEmpty"' in html

    def test_modal_present(self, html):
        assert 'id="pdModal"' in html

    def test_modal_close_button(self, html):
        assert 'id="pdModalClose"' in html

    def test_cta_strip_present(self, html):
        assert 'Need COA, Specs or a Bulk Quote?' in html

    def test_whatsapp_float_button(self, html):
        assert 'fixed bottom-6 right-5' in html

    def test_product_detail_js_loaded(self, html):
        assert 'product-detail.js' in html

    def test_no_unresolved_jinja_tags(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 3. Products JSON data injected for all 14 slugs
# ---------------------------------------------------------------------------

class TestProductsData:
    def test_json_data_present_in_page(self, client):
        for cat in CATEGORIES:
            html = detail_html(client, cat['slug'])
            assert 'id="pdData"' in html, (
                f'pdData script tag missing for {cat["slug"]}'
            )

    def test_json_data_is_valid_json(self, client):
        for cat in CATEGORIES:
            html = detail_html(client, cat['slug'])
            # Extract content of the application/json script tag
            match = re.search(
                r'<script id="pdData"[^>]*>(.*?)</script>',
                html, re.DOTALL
            )
            assert match, f'pdData not found for {cat["slug"]}'
            data = json.loads(match.group(1).strip())
            assert isinstance(data, list), f'Expected list for {cat["slug"]}'

    def test_all_categories_have_items(self, client):
        for cat in CATEGORIES:
            items = get_items(cat['slug'])
            assert len(items) > 0, (
                f'No product items for category: {cat["slug"]}'
            )

    def test_dry_extracts_count(self):
        assert len(get_items('dry-extracts')) >= 50

    def test_liquid_extracts_count(self):
        assert len(get_items('liquid-extracts')) >= 50

    def test_essential_oils_count(self):
        assert len(get_items('essential-oils')) >= 30

    def test_carrier_oils_count(self):
        assert len(get_items('carrier-oils')) >= 30

    def test_herbal_powders_count(self):
        assert len(get_items('herbal-powders')) >= 50

    def test_json_products_have_required_fields(self, client):
        required = {'name', 'botanical', 'part_used', 'industries', 'functions'}
        for cat in CATEGORIES:
            html = detail_html(client, cat['slug'])
            match = re.search(
                r'<script id="pdData"[^>]*>(.*?)</script>',
                html, re.DOTALL
            )
            data = json.loads(match.group(1).strip())
            for item in data:
                missing = required - set(item.keys())
                assert not missing, (
                    f'{cat["slug"]}: item "{item.get("name")}" missing {missing}'
                )

    def test_industries_filter_options_in_page(self, client):
        """Industry values from get_all_industries() appear as <option> in page."""
        html = detail_html(client, 'dry-extracts')
        for ind in get_all_industries('dry-extracts')[:5]:  # spot-check first 5
            assert ind in html, f'Industry option missing: {ind}'

    def test_functions_filter_options_in_page(self, client):
        """Function values from get_all_functions() appear as <option> in page."""
        html = detail_html(client, 'dry-extracts')
        for fn in get_all_functions('dry-extracts')[:5]:
            assert fn in html, f'Function option missing: {fn}'


# ---------------------------------------------------------------------------
# 4. SEO meta tags (spot-check dry-extracts + liquid-extracts)
# ---------------------------------------------------------------------------

class TestSEO:
    @pytest.mark.parametrize('slug', ['dry-extracts', 'liquid-extracts',
                                       'essential-oils', 'carrier-oils'])
    def test_meta_description_present(self, client, slug):
        html = detail_html(client, slug)
        assert 'name="description"' in html

    @pytest.mark.parametrize('slug', ['dry-extracts', 'liquid-extracts',
                                       'essential-oils', 'carrier-oils'])
    def test_canonical_contains_slug(self, client, slug):
        html = detail_html(client, slug)
        assert f'/products/{slug}' in html

    @pytest.mark.parametrize('slug', ['dry-extracts', 'liquid-extracts'])
    def test_og_tags_present(self, client, slug):
        html = detail_html(client, slug)
        assert 'property="og:title"'       in html
        assert 'property="og:description"' in html
        assert 'property="og:url"'         in html
        assert 'property="og:image"'       in html


# ---------------------------------------------------------------------------
# 5. Navigation — catalogue cards link to /products/<slug>
# ---------------------------------------------------------------------------

class TestNavigation:
    def test_catalogue_cards_link_to_detail_pages(self, client):
        html = client.get('/products').data.decode()
        for cat in CATEGORIES:
            assert f'href="/products/{cat["slug"]}"' in html, (
                f'Catalogue card link missing for {cat["slug"]}'
            )

    def test_detail_page_breadcrumb_links_back_to_catalogue(self, client):
        html = detail_html(client, 'dry-extracts')
        assert 'href="/products"' in html


# ---------------------------------------------------------------------------
# 6. data/product_items.py integrity
# ---------------------------------------------------------------------------

class TestItemsData:
    REQUIRED = ('name', 'botanical', 'part_used', 'industries', 'functions')

    def test_all_14_slugs_in_items(self):
        for cat in CATEGORIES:
            assert cat['slug'] in ITEMS, (
                f'Slug not in ITEMS: {cat["slug"]}'
            )

    def test_all_items_have_required_fields(self):
        for slug, items in ITEMS.items():
            for item in items:
                for field in self.REQUIRED:
                    assert field in item, (
                        f'{slug}: missing field "{field}" in item "{item.get("name")}"'
                    )

    def test_industries_and_functions_are_lists(self):
        for slug, items in ITEMS.items():
            for item in items:
                assert isinstance(item['industries'], list), (
                    f'{slug}: industries not a list for "{item["name"]}"'
                )
                assert isinstance(item['functions'], list), (
                    f'{slug}: functions not a list for "{item["name"]}"'
                )

    def test_no_empty_names(self):
        for slug, items in ITEMS.items():
            for item in items:
                assert item['name'].strip(), (
                    f'{slug}: empty name found'
                )

    def test_get_items_returns_correct_list(self):
        for cat in CATEGORIES:
            result = get_items(cat['slug'])
            assert result is ITEMS[cat['slug']]

    def test_get_items_returns_empty_for_unknown_slug(self):
        assert get_items('does-not-exist') == []

    def test_get_all_industries_returns_sorted_unique(self):
        industries = get_all_industries('dry-extracts')
        assert len(industries) > 0
        assert industries == sorted(set(industries))

    def test_get_all_functions_returns_sorted_unique(self):
        functions = get_all_functions('essential-oils')
        assert len(functions) > 0
        assert functions == sorted(set(functions))

    def test_all_categories_have_at_least_10_items(self):
        for cat in CATEGORIES:
            count = len(get_items(cat['slug']))
            assert count >= 10, (
                f'{cat["slug"]} has only {count} items (expected >= 10)'
            )
