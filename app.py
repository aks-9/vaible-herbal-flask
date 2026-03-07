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


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", "true").lower() == "true")
