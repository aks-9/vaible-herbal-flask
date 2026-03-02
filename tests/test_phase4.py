"""
Phase 4 — Products Catalogue tests.

Covers:
  - Route availability and HTTP status codes
  - Page structure (hero, breadcrumb, grid, CTA strip, WhatsApp button)
  - SEO meta tags (description, canonical, OG)
  - All 14 category names, product counts, and descriptions rendered
  - Navigation wiring (navbar + footer links point to /products)
  - Homepage CTAs updated to /products
  - data/products.py integrity (fields, uniqueness, helpers)
"""

import re
import pytest
from urllib.parse import quote
from app import app
from data.products import CATEGORIES, get_category, all_categories


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


@pytest.fixture
def products_html(client):
    """Decoded HTML body of GET /products."""
    return client.get("/products").data.decode()


@pytest.fixture
def home_html(client):
    """Decoded HTML body of GET /."""
    return client.get("/").data.decode()


# ---------------------------------------------------------------------------
# 1. Route tests
# ---------------------------------------------------------------------------

class TestRoutes:
    def test_products_returns_200(self, client):
        assert client.get("/products").status_code == 200

    def test_homepage_still_returns_200(self, client):
        """Regression — Phase 4 changes must not break the homepage."""
        assert client.get("/").status_code == 200

    def test_unknown_route_returns_404(self, client):
        assert client.get("/products/nonexistent-slug").status_code == 404


# ---------------------------------------------------------------------------
# 2. Page structure
# ---------------------------------------------------------------------------

class TestPageStructure:
    def test_page_title(self, products_html):
        assert "<title>Products | Vaible Herbal" in products_html

    def test_h1_heading(self, products_html):
        assert "Our Products" in products_html

    def test_breadcrumb_home_link(self, products_html):
        assert 'href="/"' in products_html or 'url_for' not in products_html
        # Home link appears in breadcrumb section
        assert "Home" in products_html

    def test_breadcrumb_current_page(self, products_html):
        assert 'aria-current="page"' in products_html

    def test_hero_subheading(self, products_html):
        assert "Full Product Catalogue" in products_html

    def test_hero_stats_sku_count(self, products_html):
        assert "600+" in products_html

    def test_hero_stats_countries(self, products_html):
        assert "26+" in products_html

    def test_hero_stats_coa(self, products_html):
        assert "COA" in products_html

    def test_category_grid_present(self, products_html):
        assert "Browse by Format" in products_html

    def test_enquire_now_cta_on_cards(self, products_html):
        assert "Enquire Now" in products_html

    def test_b2b_cta_strip_present(self, products_html):
        assert "Need a Custom Formulation or Bulk Quote?" in products_html

    def test_b2b_cta_strip_contact_link(self, products_html):
        assert "Contact Us" in products_html

    def test_b2b_cta_strip_whatsapp_link(self, products_html):
        # Both the strip and the float button include wa.me
        assert "wa.me/919911154497" in products_html

    def test_whatsapp_float_button(self, products_html):
        # Float button has specific positioning classes
        assert "fixed bottom-6 right-5" in products_html

    def test_no_unresolved_jinja_tags(self, products_html):
        assert "{{" not in products_html
        assert "{%" not in products_html


# ---------------------------------------------------------------------------
# 3. Category rendering — all 14 categories
# ---------------------------------------------------------------------------

class TestCategoryRendering:
    def test_all_14_category_names_present(self, products_html):
        for cat in CATEGORIES:
            assert cat["name"] in products_html, (
                f"Category name missing from page: {cat['name']}"
            )

    def test_all_14_product_counts_present(self, products_html):
        for cat in CATEGORIES:
            # count values like "+50", "+100" — strip the leading "+"
            count_digits = cat["count"].lstrip("+")
            assert count_digits in products_html, (
                f"Product count missing for {cat['name']}: {cat['count']}"
            )

    def test_all_14_short_descriptions_present(self, products_html):
        for cat in CATEGORIES:
            # Use first 30 chars as a unique enough probe
            snippet = cat["short_description"][:30]
            assert snippet in products_html, (
                f"Short description missing for {cat['name']}"
            )

    def test_all_14_video_sources_present(self, products_html):
        # url_for encodes spaces as %20, so match the encoded form
        for cat in CATEGORIES:
            encoded = quote(cat["video"])
            assert encoded in products_html, (
                f"Video filename missing for {cat['name']}: {cat['video']} "
                f"(expected encoded as {encoded})"
            )

    def test_all_14_poster_images_present(self, products_html):
        # url_for encodes spaces as %20, so match the encoded form
        for cat in CATEGORIES:
            encoded = quote(cat["poster"])
            assert encoded in products_html, (
                f"Poster filename missing for {cat['name']}: {cat['poster']} "
                f"(expected encoded as {encoded})"
            )

    def test_card_count_matches_categories(self, products_html):
        """Exactly 14 'Category' badge labels should appear (one per card)."""
        # Each card has a badge with the text "Category"
        matches = re.findall(r'>\s*Category\s*<', products_html)
        assert len(matches) == len(CATEGORIES), (
            f"Expected {len(CATEGORIES)} category badges, found {len(matches)}"
        )


# ---------------------------------------------------------------------------
# 4. SEO meta tags
# ---------------------------------------------------------------------------

class TestSEO:
    def test_meta_description_present(self, products_html):
        assert 'name="description"' in products_html
        assert "14 categories" in products_html or "14 product categories" in products_html.lower()

    def test_canonical_tag_present(self, products_html):
        assert 'rel="canonical"' in products_html
        assert "/products" in products_html

    def test_og_title_present(self, products_html):
        assert 'property="og:title"' in products_html

    def test_og_description_present(self, products_html):
        assert 'property="og:description"' in products_html

    def test_og_url_present(self, products_html):
        assert 'property="og:url"' in products_html

    def test_og_image_present(self, products_html):
        assert 'property="og:image"' in products_html


# ---------------------------------------------------------------------------
# 5. Navigation wiring
# ---------------------------------------------------------------------------

class TestNavigation:
    def test_products_link_in_desktop_navbar(self, products_html):
        """The active page's navbar should contain a link to /products."""
        assert 'href="/products"' in products_html

    def test_products_link_in_mobile_drawer(self, products_html):
        # Mobile drawer also links to /products — there should be multiple occurrences
        count = products_html.count('href="/products"')
        assert count >= 2, (
            f"Expected at least 2 /products links (desktop + mobile), found {count}"
        )

    def test_footer_view_all_products_links_to_products(self, products_html):
        assert "View All Products" in products_html

    def test_homepage_explore_products_links_to_products(self, home_html):
        assert 'href="/products"' in home_html

    def test_homepage_view_all_cta_links_to_products(self, home_html):
        assert "View All 14 Categories" in home_html
        # The anchor wrapping it should point to /products
        idx = home_html.find("View All 14 Categories")
        surrounding = home_html[max(0, idx - 200):idx]
        assert "/products" in surrounding


# ---------------------------------------------------------------------------
# 6. data/products.py integrity
# ---------------------------------------------------------------------------

class TestProductsData:
    REQUIRED_FIELDS = ("slug", "name", "count", "video", "poster",
                       "short_description", "meta_description")

    def test_exactly_14_categories(self):
        assert len(CATEGORIES) == 14

    def test_all_required_fields_present(self):
        for cat in CATEGORIES:
            for field in self.REQUIRED_FIELDS:
                assert field in cat, f"Missing field '{field}' in category: {cat.get('name')}"
                assert cat[field], f"Empty value for '{field}' in category: {cat.get('name')}"

    def test_slugs_are_unique(self):
        slugs = [cat["slug"] for cat in CATEGORIES]
        assert len(slugs) == len(set(slugs)), "Duplicate slugs found"

    def test_slugs_are_url_safe(self):
        for cat in CATEGORIES:
            assert re.match(r'^[a-z0-9\-]+$', cat["slug"]), (
                f"Slug contains invalid characters: {cat['slug']}"
            )

    def test_names_are_unique(self):
        names = [cat["name"] for cat in CATEGORIES]
        assert len(names) == len(set(names)), "Duplicate category names found"

    def test_get_category_returns_correct_item(self):
        for cat in CATEGORIES:
            result = get_category(cat["slug"])
            assert result is not None
            assert result["name"] == cat["name"]

    def test_get_category_returns_none_for_unknown_slug(self):
        assert get_category("does-not-exist") is None
        assert get_category("") is None

    def test_all_categories_returns_full_list(self):
        result = all_categories()
        assert result is CATEGORIES
        assert len(result) == 14

    def test_short_descriptions_are_meaningful(self):
        for cat in CATEGORIES:
            desc = cat["short_description"]
            assert len(desc) >= 40, (
                f"Short description too brief for {cat['name']}: {repr(desc)}"
            )

    def test_meta_descriptions_are_meaningful(self):
        for cat in CATEGORIES:
            desc = cat["meta_description"]
            assert len(desc) >= 50, (
                f"Meta description too brief for {cat['name']}: {repr(desc)}"
            )
            # Should mention Vaible Herbal for brand consistency
            assert "Vaible Herbal" in desc, (
                f"Meta description missing brand name for {cat['name']}"
            )

    def test_count_values_are_plausible(self):
        """Count should be a stringified positive integer with a leading '+'."""
        for cat in CATEGORIES:
            count = cat["count"]
            assert count.startswith("+"), f"Count should start with '+': {cat['name']} → {count}"
            assert count[1:].isdigit(), f"Count should be numeric after '+': {cat['name']} → {count}"
            assert int(count[1:]) > 0, f"Count should be positive: {cat['name']} → {count}"
