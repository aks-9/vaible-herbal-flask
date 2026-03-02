from flask import Flask, render_template
from dotenv import load_dotenv
import os
from data.products import all_categories

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("pages/products.html", categories=all_categories())


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG", "true").lower() == "true")
