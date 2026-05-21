# My Site - Django Blog Project

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

Aplicació web desenvolupada amb Django per gestionar un blog amb publicacions, autors i etiquetes.

---

# Features

- Sistema de publicacions
- Gestió d'autors
- Sistema d'etiquetes
- Visualització detallada de posts
- Plantilles HTML dinàmiques
- Panell d'administració Django
- Sistema de rutes amb Django URLs
- ORM de Django
- Generació automàtica de documentació amb Pydoc
- GitHub Actions integrat

---

# Technologies

- Python 3.12
- Django 6.0
- SQLite3
- HTML5
- CSS3

---

# Project Structure

```text
my_site/
│
├── blog/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   └── 404.html
│
├── docs/
├── .github/
│   └── workflows/
│       └── pydoc.yml
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
