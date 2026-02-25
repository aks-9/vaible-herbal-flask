# Vaible Herbal — Flask Website

B2B herbal products website built with Python Flask and Tailwind CSS.

## Tech Stack

- **Backend:** Python 3.12+ / Flask 3.1
- **Frontend:** Tailwind CSS, vanilla JS
- **Deployment:** Render / Railway (WSGI via Gunicorn)

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/vaible-herbal-flask.git
cd vaible-herbal-flask

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your values

# 5. Run the development server
python app.py
```

Visit `http://localhost:5000`

## Project Structure

```
vaible-herbal-flask/
├── app.py                  # Flask application + routes
├── data/                   # Product data, nav config
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Shared layout (navbar, footer, dark mode)
│   ├── index.html          # Homepage
│   └── pages/              # Subpages
├── static/
│   ├── css/output.css      # Compiled Tailwind CSS
│   ├── js/                 # Client-side scripts
│   └── images/             # Site images and videos
└── requirements.txt
```

## Build Phases

- [x] Phase 1 — Project foundation
- [ ] Phase 2 — Tailwind + base layout
- [ ] Phase 3 — Homepage
- [ ] Phase 4 — Products catalogue
- [ ] Phase 5 — Product detail pages
- [ ] Phase 6 — About section
- [ ] Phase 7 — Innovation section
- [ ] Phase 8 — Resources section
- [ ] Phase 9 — Contact + form handling
- [ ] Phase 10 — SEO & meta tags
- [ ] Phase 11 — Deployment
