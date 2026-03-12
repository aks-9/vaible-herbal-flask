"""
Phase 8 — Resources Section tests.

Covers:
  - Route availability for all 5 resource pages (200 OK)
  - 404 for unknown routes
  - Page structure (breadcrumb, H1, key content sections)
  - SEO meta tags (description, canonical, OG)
  - Navigation: navbar + mobile drawer links wired to correct routes
  - Regression: all previous phase routes still return 200
  - Blog posts data helpers
"""

import json
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
# Route paths used throughout tests
# ---------------------------------------------------------------------------

RESOURCES_ROUTES = [
    '/resources/news-blogs',
    '/resources/webinar',
    '/resources/events',
    '/resources/career',
    '/resources/brochure',
]

RESOURCES_WITH_SLUGS = [
    ('/resources/news-blogs',  'news-blogs'),
    ('/resources/webinar',     'webinar'),
    ('/resources/events',      'events'),
    ('/resources/career',      'career'),
    ('/resources/brochure',    'brochure'),
]


# ---------------------------------------------------------------------------
# 1. Route tests
# ---------------------------------------------------------------------------

class TestRoutes:
    @pytest.mark.parametrize('path', RESOURCES_ROUTES)
    def test_resource_page_returns_200(self, client, path):
        assert client.get(path).status_code == 200

    def test_unknown_route_returns_404(self, client):
        assert client.get('/resources/does-not-exist').status_code == 404

    # Regression — all previous phases
    def test_homepage_still_200(self, client):
        assert client.get('/').status_code == 200

    def test_products_still_200(self, client):
        assert client.get('/products').status_code == 200

    def test_about_who_we_are_still_200(self, client):
        assert client.get('/about/who-we-are').status_code == 200

    def test_innovation_applied_research_still_200(self, client):
        assert client.get('/innovation/applied-research').status_code == 200


# ---------------------------------------------------------------------------
# 2. News & Blogs page
# ---------------------------------------------------------------------------

class TestNewsBlogsPage:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/resources/news-blogs')

    def test_title_has_news(self, html):
        assert 'News' in html
        assert 'Vaible Herbal' in html

    def test_h1_has_news(self, html):
        assert '<h1' in html
        assert 'News' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'Resources' in html
        assert 'aria-current="page"' in html

    def test_category_pills_present(self, html):
        assert 'quality-systems' in html
        assert 'process' in html
        assert 'analytical' in html
        assert 'regulatory' in html
        assert 'sustainability' in html

    def test_search_input_present(self, html):
        assert 'id="nbSearch"' in html

    def test_nbgrid_present(self, html):
        assert 'id="nbGrid"' in html

    def test_nbdata_script_tag_present(self, html):
        assert 'id="nbData"' in html
        assert 'type="application/json"' in html

    def test_nbdata_is_valid_json(self, html):
        start = html.find('id="nbData"')
        assert start != -1
        tag_end = html.find('>', start)
        close_tag = html.find('</script>', tag_end)
        json_str = html[tag_end + 1:close_tag].strip()
        posts = json.loads(json_str)
        assert isinstance(posts, list)
        assert len(posts) > 0

    def test_posts_have_required_fields(self, html):
        start = html.find('id="nbData"')
        tag_end = html.find('>', start)
        close_tag = html.find('</script>', tag_end)
        posts = json.loads(html[tag_end + 1:close_tag].strip())
        for post in posts:
            assert 'id' in post
            assert 'title' in post
            assert 'category' in post
            assert 'date' in post
            assert 'summary' in post
            assert 'content' in post
            assert 'tags' in post

    def test_scripts_loads_news_blogs_js(self, html):
        assert 'news-blogs.js' in html

    def test_modal_overlay_present(self, html):
        assert 'id="nbOverlay"' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 3. Webinar page
# ---------------------------------------------------------------------------

class TestWebinarPage:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/resources/webinar')

    def test_title_has_webinar(self, html):
        assert 'Webinar' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Vaible Herbal Webinars' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'Resources' in html
        assert 'aria-current="page"' in html

    def test_featured_webinar_section(self, html):
        assert 'Featured Webinar' in html
        assert 'Building Export-Ready Herbal Specifications' in html

    def test_why_attend_section(self, html):
        benefits = [
            'Compliance-first frameworks',
            'Better supplier evaluation',
            'QC',
            'Formulation insights',
        ]
        for b in benefits:
            assert b in html, f'Missing benefit: {b}'

    def test_upcoming_webinars_4_titles(self, html):
        assert 'Heavy Metals' in html
        assert 'Dry Extracts' in html
        assert 'Global Documentation' in html
        assert 'Carrier Oils' in html

    def test_on_demand_section(self, html):
        assert 'On-Demand' in html or 'On Demand' in html
        assert 'Essential Oils' in html

    def test_faq_section_3_questions(self, html):
        assert 'Is registration free' in html
        assert 'get a recording' in html
        assert 'request a topic' in html

    def test_register_modal_present(self, html):
        assert 'id="webinarModal"' in html

    def test_cta_strip_present(self, html):
        assert 'Want a webinar' in html or 'specific ingredient' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 4. Events page
# ---------------------------------------------------------------------------

class TestEventsPage:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/resources/events')

    def test_title_has_events(self, html):
        assert 'Events' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Meet us' in html or 'sourcing' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'Resources' in html
        assert 'aria-current="page"' in html

    def test_upcoming_events_section(self, html):
        assert 'Upcoming Events' in html
        assert 'Ingredients' in html and 'Botanicals' in html
        assert 'Standardization' in html or 'Documentation' in html

    def test_upcoming_events_count(self, html):
        # Both Dubai and Online events should be present
        assert 'Dubai' in html
        assert 'Online' in html

    def test_past_events_section(self, html):
        assert 'Past Events' in html
        assert 'Botanical Supply Chain Forum' in html
        assert 'Private Buyer Meetings' in html or 'Frankfurt' in html

    def test_what_to_expect_section(self, html):
        expects = [
            'COA',
            'Sampling',
            'Custom specs',
            'Export packaging',
        ]
        for e in expects:
            assert e in html, f'Missing expect item: {e}'

    def test_filter_bar_present(self, html):
        assert 'All Types' in html or 'Exhibition' in html
        assert 'All Regions' in html or 'India' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 5. Career page
# ---------------------------------------------------------------------------

class TestCareerPage:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/resources/career')

    def test_title_has_career(self, html):
        assert 'Career' in html
        assert 'Vaible Herbal' in html

    def test_h1_has_build_the_future(self, html):
        assert '<h1' in html
        assert 'Build the future' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'Resources' in html
        assert 'aria-current="page"' in html

    def test_why_vaible_section_4_cards(self, html):
        cards = [
            'Quality',
            'Operational Excellence',
            'Customer-First',
            'Global Mindset',
        ]
        for c in cards:
            assert c in html, f'Missing card: {c}'

    def test_culture_section(self, html):
        assert 'How We Work' in html or 'Culture' in html
        assert 'High ownership' in html

    def test_open_roles_section(self, html):
        assert 'id="open-roles"' in html

    def test_4_role_titles_present(self, html):
        roles = [
            'QC Executive',
            'Export Operations Coordinator',
            'International Sales Executive',
            'Regulatory Documentation Specialist',
        ]
        for role in roles:
            assert role in html, f'Missing role: {role}'

    def test_hiring_process_steps(self, html):
        for step in ['01', '02', '03', '04']:
            assert step in html, f'Missing step number: {step}'

    def test_apply_form_present(self, html):
        assert 'id="careerApplyForm"' in html
        assert 'id="applyRoleField"' in html
        assert 'id="apply-now"' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 6. Brochure page
# ---------------------------------------------------------------------------

class TestBrochurePage:
    @pytest.fixture
    def html(self, client):
        return get_html(client, '/resources/brochure')

    def test_title_has_brochure(self, html):
        assert 'Brochure' in html
        assert 'Vaible Herbal' in html

    def test_h1_present(self, html):
        assert '<h1' in html
        assert 'Brochures' in html or 'Documentation' in html

    def test_breadcrumb_present(self, html):
        assert 'href="/"' in html
        assert 'Resources' in html
        assert 'aria-current="page"' in html

    def test_4_document_cards(self, html):
        docs = [
            'Company Overview',
            'Product Catalogue',
            'Quality',
            'Ingredient Specification',
        ]
        for doc in docs:
            assert doc in html, f'Missing document card: {doc}'

    def test_policy_note_present(self, html):
        assert 'request' in html.lower()
        assert 'B2B' in html or 'policy' in html.lower()

    def test_cta_strip_present(self, html):
        assert 'COA' in html or 'specs' in html.lower()
        assert 'Contact Us' in html

    def test_no_jinja_leakage(self, html):
        assert '{{' not in html
        assert '{%' not in html


# ---------------------------------------------------------------------------
# 7. SEO meta tags — all 5 pages
# ---------------------------------------------------------------------------

class TestSEO:
    @pytest.mark.parametrize('path', RESOURCES_ROUTES)
    def test_meta_description(self, client, path):
        html = get_html(client, path)
        assert 'name="description"' in html

    @pytest.mark.parametrize('path,slug', RESOURCES_WITH_SLUGS)
    def test_canonical_contains_slug(self, client, path, slug):
        html = get_html(client, path)
        assert f'/resources/{slug}' in html

    @pytest.mark.parametrize('path', RESOURCES_ROUTES)
    def test_og_title_present(self, client, path):
        html = get_html(client, path)
        assert 'property="og:title"' in html

    @pytest.mark.parametrize('path', RESOURCES_ROUTES)
    def test_og_description_present(self, client, path):
        html = get_html(client, path)
        assert 'property="og:description"' in html

    @pytest.mark.parametrize('path', RESOURCES_ROUTES)
    def test_og_url_present(self, client, path):
        html = get_html(client, path)
        assert 'property="og:url"' in html


# ---------------------------------------------------------------------------
# 8. Navigation — resource links wired correctly
# ---------------------------------------------------------------------------

class TestNavigation:
    def test_desktop_navbar_news_blogs_link(self, client):
        html = get_html(client, '/')
        assert 'href="/resources/news-blogs"' in html

    def test_desktop_navbar_webinar_link(self, client):
        html = get_html(client, '/')
        assert 'href="/resources/webinar"' in html

    def test_desktop_navbar_events_link(self, client):
        html = get_html(client, '/')
        assert 'href="/resources/events"' in html

    def test_desktop_navbar_career_link(self, client):
        html = get_html(client, '/')
        assert 'href="/resources/career"' in html

    def test_desktop_navbar_brochure_link(self, client):
        html = get_html(client, '/')
        assert 'href="/resources/brochure"' in html

    def test_mobile_drawer_news_blogs_link(self, client):
        html = get_html(client, '/')
        assert html.count('href="/resources/news-blogs"') >= 2  # desktop + mobile

    def test_mobile_drawer_career_link(self, client):
        html = get_html(client, '/')
        assert html.count('href="/resources/career"') >= 2  # desktop + mobile + footer

    def test_footer_career_link_wired(self, client):
        html = get_html(client, '/')
        assert 'href="/resources/career"' in html

    def test_breadcrumbs_link_home(self, client):
        for path in RESOURCES_ROUTES:
            html = get_html(client, path)
            assert 'href="/"' in html, f'Home breadcrumb missing on {path}'


# ---------------------------------------------------------------------------
# 9. Blog posts data helpers
# ---------------------------------------------------------------------------

class TestBlogPostsData:
    VALID_CATEGORIES = {'quality-systems', 'process', 'analytical', 'regulatory', 'sustainability'}

    def test_get_all_posts_returns_list(self):
        from data.blog_posts import get_all_posts
        posts = get_all_posts()
        assert isinstance(posts, list)
        assert len(posts) > 0

    def test_all_posts_have_required_fields(self):
        from data.blog_posts import get_all_posts
        for post in get_all_posts():
            assert 'id' in post
            assert 'title' in post
            assert 'category' in post
            assert 'date' in post
            assert 'summary' in post
            assert 'content' in post
            assert 'tags' in post

    def test_categories_are_valid_values(self):
        from data.blog_posts import get_all_posts
        for post in get_all_posts():
            assert post['category'] in self.VALID_CATEGORIES, \
                f'Invalid category: {post["category"]}'

    def test_dates_are_strings(self):
        from data.blog_posts import get_all_posts
        for post in get_all_posts():
            assert isinstance(post['date'], str)
            # Basic date format check YYYY-MM-DD
            assert len(post['date']) == 10
            assert post['date'][4] == '-'
            assert post['date'][7] == '-'

    def test_tags_are_lists(self):
        from data.blog_posts import get_all_posts
        for post in get_all_posts():
            assert isinstance(post['tags'], list)

    def test_all_5_categories_represented(self):
        from data.blog_posts import get_all_posts
        cats = {post['category'] for post in get_all_posts()}
        assert cats == self.VALID_CATEGORIES, \
            f'Missing categories: {self.VALID_CATEGORIES - cats}'

    def test_posts_sorted_newest_first(self):
        from data.blog_posts import get_all_posts
        posts = get_all_posts()
        dates = [p['date'] for p in posts]
        assert dates == sorted(dates, reverse=True)

    def test_get_post_by_id_returns_correct_post(self):
        from data.blog_posts import get_all_posts, get_post_by_id
        posts = get_all_posts()
        for post in posts[:3]:
            found = get_post_by_id(post['id'])
            assert found is not None
            assert found['id'] == post['id']
            assert found['title'] == post['title']

    def test_get_post_by_id_returns_none_for_unknown(self):
        from data.blog_posts import get_post_by_id
        assert get_post_by_id(99999) is None

    def test_ids_are_unique(self):
        from data.blog_posts import get_all_posts
        ids = [p['id'] for p in get_all_posts()]
        assert len(ids) == len(set(ids))

    def test_all_8_posts_present(self):
        from data.blog_posts import get_all_posts
        assert len(get_all_posts()) == 8

    def test_content_is_non_empty_string(self):
        from data.blog_posts import get_all_posts
        for post in get_all_posts():
            assert isinstance(post['content'], str)
            assert len(post['content']) > 100
