from flask import Flask, render_template, abort
from dotenv import load_dotenv
import os
from datetime import date
from data.products import all_categories, get_category
from data.product_items import get_items, get_all_industries, get_all_functions

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")

SITE_URL = "https://www.vaibleherbal.in"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template(
        "pages/products.html",
        categories=all_categories(),
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "Products", "url": SITE_URL + "/products"},
        ],
    )


@app.route("/products/<slug>")
def product_detail(slug):
    category = get_category(slug)
    if category is None:
        abort(404)
    return render_template(
        "pages/product_detail.html",
        category=category,
        items=get_items(slug),
        industries=get_all_industries(slug),
        functions=get_all_functions(slug),
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "Products", "url": SITE_URL + "/products"},
            {"name": category["name"], "url": f"{SITE_URL}/products/{slug}"},
        ],
    )


# ---------------------------------------------------------------------------
# About section routes
# ---------------------------------------------------------------------------

@app.route("/about/who-we-are")
def who_we_are():
    return render_template(
        "pages/about/who-we-are.html",
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "About Us", "url": SITE_URL + "/about/who-we-are"},
            {"name": "Who We Are", "url": SITE_URL + "/about/who-we-are"},
        ],
    )


@app.route("/about/vision-mission")
def vision_mission():
    return render_template(
        "pages/about/vision-mission.html",
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "About Us", "url": SITE_URL + "/about/who-we-are"},
            {"name": "Vision & Mission", "url": SITE_URL + "/about/vision-mission"},
        ],
    )


@app.route("/about/management")
def management():
    return render_template(
        "pages/about/management.html",
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "About Us", "url": SITE_URL + "/about/who-we-are"},
            {"name": "Management", "url": SITE_URL + "/about/management"},
        ],
    )


@app.route("/about/csr")
def csr():
    return render_template(
        "pages/about/csr.html",
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "About Us", "url": SITE_URL + "/about/who-we-are"},
            {"name": "CSR", "url": SITE_URL + "/about/csr"},
        ],
    )


# ---------------------------------------------------------------------------
# Innovation section routes
# ---------------------------------------------------------------------------

_INNOVATION_CRUMBS = [
    {"name": "Home", "url": SITE_URL + "/"},
    {"name": "Innovation", "url": SITE_URL + "/innovation/applied-research"},
]


@app.route("/innovation/applied-research")
def applied_research():
    return render_template(
        "pages/innovation/applied-research.html",
        breadcrumbs=_INNOVATION_CRUMBS + [
            {"name": "Applied Research", "url": SITE_URL + "/innovation/applied-research"},
        ],
    )


@app.route("/innovation/phytochemical-understanding")
def phytochemical_understanding():
    return render_template(
        "pages/innovation/phytochemical-understanding.html",
        breadcrumbs=_INNOVATION_CRUMBS + [
            {"name": "Phytochemical Understanding", "url": SITE_URL + "/innovation/phytochemical-understanding"},
        ],
    )


@app.route("/innovation/product-development-framework")
def product_development_framework():
    return render_template(
        "pages/innovation/product-development-framework.html",
        breadcrumbs=_INNOVATION_CRUMBS + [
            {"name": "Product Development Framework", "url": SITE_URL + "/innovation/product-development-framework"},
        ],
    )


@app.route("/innovation/formulation-application-insights")
def formulation_application_insights():
    return render_template(
        "pages/innovation/formulation-application-insights.html",
        breadcrumbs=_INNOVATION_CRUMBS + [
            {"name": "Formulation & Application Insights", "url": SITE_URL + "/innovation/formulation-application-insights"},
        ],
    )


@app.route("/innovation/quality-systems-ci")
def quality_systems_ci():
    return render_template(
        "pages/innovation/quality-systems-ci.html",
        breadcrumbs=_INNOVATION_CRUMBS + [
            {"name": "Quality Systems & CI", "url": SITE_URL + "/innovation/quality-systems-ci"},
        ],
    )


@app.route("/innovation/future-readiness")
def future_readiness():
    return render_template(
        "pages/innovation/future-readiness.html",
        breadcrumbs=_INNOVATION_CRUMBS + [
            {"name": "Future Readiness", "url": SITE_URL + "/innovation/future-readiness"},
        ],
    )


# ---------------------------------------------------------------------------
# Resources section routes
# ---------------------------------------------------------------------------

_RESOURCES_CRUMBS = [
    {"name": "Home", "url": SITE_URL + "/"},
    {"name": "Resources", "url": SITE_URL + "/resources/news-blogs"},
]


@app.route("/resources/news-blogs")
def news_blogs():
    from data.blog_posts import get_all_posts
    return render_template(
        "pages/resources/news-blogs.html",
        posts=get_all_posts(),
        breadcrumbs=_RESOURCES_CRUMBS + [
            {"name": "News & Blogs", "url": SITE_URL + "/resources/news-blogs"},
        ],
    )


@app.route("/resources/webinar")
def webinar():
    return render_template(
        "pages/resources/webinar.html",
        breadcrumbs=_RESOURCES_CRUMBS + [
            {"name": "Webinar", "url": SITE_URL + "/resources/webinar"},
        ],
    )


@app.route("/resources/events")
def events():
    return render_template(
        "pages/resources/events.html",
        breadcrumbs=_RESOURCES_CRUMBS + [
            {"name": "Events", "url": SITE_URL + "/resources/events"},
        ],
    )


@app.route("/resources/career")
def career():
    return render_template(
        "pages/resources/career.html",
        breadcrumbs=_RESOURCES_CRUMBS + [
            {"name": "Career", "url": SITE_URL + "/resources/career"},
        ],
    )


@app.route("/resources/brochure")
def brochure():
    return render_template(
        "pages/resources/brochure.html",
        breadcrumbs=_RESOURCES_CRUMBS + [
            {"name": "Brochure", "url": SITE_URL + "/resources/brochure"},
        ],
    )


# ---------------------------------------------------------------------------
# Contact route
# ---------------------------------------------------------------------------

@app.route("/contact")
def contact():
    return render_template(
        "pages/contact.html",
        breadcrumbs=[
            {"name": "Home", "url": SITE_URL + "/"},
            {"name": "Contact Us", "url": SITE_URL + "/contact"},
        ],
    )


# ---------------------------------------------------------------------------
# SEO utility routes
# ---------------------------------------------------------------------------

@app.route("/robots.txt")
def robots_txt():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    return content, 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.route("/sitemap.xml")
def sitemap_xml():
    today = date.today().isoformat()

    static_pages = [
        ("/",                                         "1.0", "weekly"),
        ("/products",                                 "0.9", "monthly"),
        ("/about/who-we-are",                         "0.7", "monthly"),
        ("/about/vision-mission",                     "0.7", "monthly"),
        ("/about/management",                         "0.7", "monthly"),
        ("/about/csr",                                "0.7", "monthly"),
        ("/innovation/applied-research",              "0.7", "monthly"),
        ("/innovation/phytochemical-understanding",   "0.7", "monthly"),
        ("/innovation/product-development-framework", "0.7", "monthly"),
        ("/innovation/formulation-application-insights", "0.7", "monthly"),
        ("/innovation/quality-systems-ci",            "0.7", "monthly"),
        ("/innovation/future-readiness",              "0.7", "monthly"),
        ("/resources/news-blogs",                     "0.6", "weekly"),
        ("/resources/webinar",                        "0.6", "monthly"),
        ("/resources/events",                         "0.6", "monthly"),
        ("/resources/career",                         "0.6", "monthly"),
        ("/resources/brochure",                       "0.6", "monthly"),
        ("/contact",                                  "0.8", "monthly"),
    ]

    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

    for path, priority, changefreq in static_pages:
        xml_parts.append(
            f"  <url>\n"
            f"    <loc>{SITE_URL}{path}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )

    for cat in all_categories():
        xml_parts.append(
            f"  <url>\n"
            f"    <loc>{SITE_URL}/products/{cat['slug']}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>0.8</priority>\n"
            f"  </url>"
        )

    xml_parts.append("</urlset>")
    return "\n".join(xml_parts), 200, {"Content-Type": "application/xml; charset=utf-8"}


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", "true").lower() == "true")
