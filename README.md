# Vaible Herbal — Flask Website

B2B herbal ingredients website built with Python Flask and Tailwind CSS v3.
Covers the full company: products catalogue, about, innovation, resources, and contact.

## Tech Stack

- **Backend:** Python 3.12+ / Flask 3.1
- **Frontend:** Tailwind CSS v3, vanilla JS (no jQuery, no framework)
- **Templating:** Jinja2
- **Animations:** GSAP 3 + ScrollTrigger
- **Chatbot:** Google Gemini API (`gemini-2.5-flash`) via `google-genai`
- **Maps:** jsvectormap (world map, CDN)
- **Deployment:** PythonAnywhere (WSGI via `wsgi.py`)

## Features

- 14-category product catalogue with 700+ SKUs, search, filter, and modal detail view
- Hero slider, dark mode (persisted via `localStorage`), mobile drawer navigation
- About, Innovation, Resources, and Contact sections — 20+ pages
- **World map** — highlights 26+ export countries on the homepage
- **AI chatbot** — Gemini-powered floating widget, trained on Vaible Herbal's products and contact info
- **GSAP animations** — hero entrance, stats count-up, scroll-triggered card stagger and fade-ins
- SEO: per-page meta/OG tags, JSON-LD (Organization + BreadcrumbList), `robots.txt`, `sitemap.xml`
- Custom 404 page
- 489 pytest tests across 7 test modules

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/aks-9/vaible-herbal-flask.git
cd vaible-herbal-flask

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env — set SECRET_KEY and GEMINI_API_KEY

# 5. Run the development server
python app.py
```

Visit `http://localhost:5000`

### Gemini API Key

The chatbot requires a free Gemini API key:
1. Go to [aistudio.google.com](https://aistudio.google.com) → Get API key
2. Add `GEMINI_API_KEY=your-key` to your `.env` file

## Build CSS (if you change templates or input.css)

```bash
node_modules/.bin/tailwindcss -i static/css/input.css -o static/css/output.css --minify
```

## Run Tests

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

## Project Structure

```
vaible-herbal-flask/
├── app.py                      # Flask routes, chatbot, sitemap, robots.txt, 404 handler
├── wsgi.py                     # WSGI entry point for PythonAnywhere
├── data/
│   ├── products.py             # 14 product categories (slug, name, meta, etc.)
│   ├── product_items.py        # 700+ product items across all categories
│   └── blog_posts.py           # 8 blog posts for News & Blogs page
├── templates/
│   ├── base.html               # Shared layout (navbar, footer, dark mode, chatbot widget)
│   ├── 404.html                # Custom 404 page
│   ├── index.html              # Homepage (hero, stats, company intro, world map, products)
│   └── pages/
│       ├── products.html       # Full product catalogue
│       ├── product_detail.html # Category detail with search/filter/modal
│       ├── contact.html        # Contact form, locations, map
│       ├── about/              # who-we-are, vision-mission, management, csr
│       ├── innovation/         # applied-research, phytochemical-understanding,
│       │                       # product-development-framework,
│       │                       # formulation-application-insights,
│       │                       # quality-systems-ci, future-readiness
│       └── resources/          # news-blogs, webinar, events, career, brochure
├── static/
│   ├── css/
│   │   ├── input.css           # Tailwind source
│   │   └── output.css          # Compiled Tailwind (committed, no CI yet)
│   ├── js/
│   │   ├── nav.js              # Dropdowns, mobile drawer, dark mode toggle
│   │   ├── home.js             # Hero slider
│   │   ├── animations.js       # GSAP scroll animations (global)
│   │   ├── chat.js             # Gemini chatbot widget
│   │   ├── world-map.js        # jsvectormap world map (homepage)
│   │   ├── product-detail.js   # Search/filter/sort + XSS-safe modal
│   │   └── news-blogs.js       # Blog search/filter/sort + modal
│   └── images/
│       ├── hero/               # slide1-4.jpg
│       ├── category/           # 14 × mp4 + PNG poster
│       └── logo/               # logo-vaible-herbal.png
├── tests/
│   ├── test_phase4.py          # 46 tests — products catalogue
│   ├── test_phase5.py          # 54 tests — product detail pages
│   ├── test_phase6.py          # 69 tests — about section
│   ├── test_phase7.py          # 91 tests — innovation section
│   ├── test_phase8.py          # 105 tests — resources section
│   ├── test_phase9.py          # 62 tests — contact + forms
│   └── test_phase10.py         # 62 tests — SEO & meta
├── requirements.txt
├── requirements-dev.txt        # pytest
├── tailwind.config.js
├── .env.example
└── .gitignore
```

## Build Phases

- [x] Phase 1 — Project foundation
- [x] Phase 2 — Tailwind CSS + base layout
- [x] Phase 3 — Homepage
- [x] Phase 4 — Products catalogue
- [x] Phase 5 — Product detail pages
- [x] Phase 6 — About section
- [x] Phase 7 — Innovation section
- [x] Phase 8 — Resources section
- [x] Phase 9 — Contact + form handling
- [x] Phase 10 — SEO & meta tags
- [x] GSAP animations
- [x] Gemini AI chatbot
- [x] World map (homepage)
- [x] Phase 11 — Deployment (PythonAnywhere)
