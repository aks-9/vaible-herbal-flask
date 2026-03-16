from flask import Flask, render_template, abort
from dotenv import load_dotenv
import os
from data.products import all_categories, get_category
from data.product_items import get_items, get_all_industries, get_all_functions

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("pages/products.html", categories=all_categories())


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
    )


# ---------------------------------------------------------------------------
# About section routes
# ---------------------------------------------------------------------------

@app.route("/about/who-we-are")
def who_we_are():
    return render_template("pages/about/who-we-are.html")


@app.route("/about/vision-mission")
def vision_mission():
    return render_template("pages/about/vision-mission.html")


@app.route("/about/management")
def management():
    return render_template("pages/about/management.html")


@app.route("/about/csr")
def csr():
    return render_template("pages/about/csr.html")


# ---------------------------------------------------------------------------
# Innovation section routes
# ---------------------------------------------------------------------------

@app.route("/innovation/applied-research")
def applied_research():
    return render_template("pages/innovation/applied-research.html")


@app.route("/innovation/phytochemical-understanding")
def phytochemical_understanding():
    return render_template("pages/innovation/phytochemical-understanding.html")


@app.route("/innovation/product-development-framework")
def product_development_framework():
    return render_template("pages/innovation/product-development-framework.html")


@app.route("/innovation/formulation-application-insights")
def formulation_application_insights():
    return render_template("pages/innovation/formulation-application-insights.html")


@app.route("/innovation/quality-systems-ci")
def quality_systems_ci():
    return render_template("pages/innovation/quality-systems-ci.html")


@app.route("/innovation/future-readiness")
def future_readiness():
    return render_template("pages/innovation/future-readiness.html")


# ---------------------------------------------------------------------------
# Resources section routes
# ---------------------------------------------------------------------------

@app.route("/resources/news-blogs")
def news_blogs():
    from data.blog_posts import get_all_posts
    return render_template("pages/resources/news-blogs.html", posts=get_all_posts())


@app.route("/resources/webinar")
def webinar():
    return render_template("pages/resources/webinar.html")


@app.route("/resources/events")
def events():
    return render_template("pages/resources/events.html")


@app.route("/resources/career")
def career():
    return render_template("pages/resources/career.html")


@app.route("/resources/brochure")
def brochure():
    return render_template("pages/resources/brochure.html")


# ---------------------------------------------------------------------------
# Contact route
# ---------------------------------------------------------------------------

@app.route("/contact")
def contact():
    return render_template("pages/contact.html")


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", "true").lower() == "true")
