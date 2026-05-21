# My Site - Projecte Blog amb Django

<p align="center">
  Aplicació web desenvolupada amb Django per gestionar publicacions, autors i etiquetes.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![SQLite](https://img.shields.io/badge/Base%20de%20Dades-SQLite-lightgrey)
![Estat](https://img.shields.io/badge/Estat-Completat-success)
![Llicència](https://img.shields.io/badge/Llicència-MIT-yellow)

</p>

---

# Descripció del Projecte

Aquest projecte consisteix en una aplicació web desenvolupada amb Django que permet gestionar un sistema de blog complet amb publicacions, autors i etiquetes.

El projecte utilitza:

- Django Framework
- SQLite3
- Templates HTML
- Sistema de rutes Django
- Django ORM
- GitHub Actions
- Pydoc

---

# Característiques Principals

- Sistema de publicacions
- Visualització detallada de posts
- Gestió d'autors
- Sistema d'etiquetes
- Templates dinàmics
- Panell d'administració Django
- Arquitectura MVC
- ORM amb Django Models
- Documentació automàtica amb Pydoc
- Integració contínua amb GitHub Actions

---

# Arquitectura de l'Aplicació

graph TD
    Client["Client / Navegador"]
    URLs["Django URLs<br/>urls.py"]
    Views["Views<br/>views.py"]
    Models["Models<br/>models.py"]
    DB["Base de Dades<br/>SQLite3"]
    
    Client -->|HTTP Request| URLs
    URLs --> Views
    Views --> Models
    Models --> DB
    
    DB -->|QuerySet| Models
    Models -->|Dades| Views
    Views -->|HTTP Response| Client
    
    style Client fill:#e1f5fe
    style URLs fill:#f3e5f5
    style Views fill:#e8f5e9
    style Models fill:#fff3e0
    style DB fill:#fce4ec

---

# Diagrama de Base de Dades

erDiagram
    AUTHOR ||--o{ POST : "1:N"
    POST }o--|| TAG : "N:M"
    
    AUTHOR {
        int id PK
        string first_name
        string last_name
        string email
    }
    
    POST {
        int id PK
        string title
        string excerpt
        string image_name
        date date
        string slug
        text content
        int author_id FK
    }
    
    TAG {
        int id PK
        string caption
    }

---

# Tecnologies Utilitzades

| Tecnologia | Descripció |
|---|---|
| Python 3.12 | Llenguatge principal |
| Django 6 | Framework web |
| SQLite3 | Base de dades |
| HTML5 | Estructura frontend |
| CSS3 | Estils |
| GitHub Actions | CI/CD |
| Pydoc | Documentació automàtica |

---

# Estructura del Projecte

```text
my_site/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── docs/
│
├── .github/
│   └── workflows/
│       └── pydoc.yml
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

# Instal·lació

## Clonar Repositori

```bash
git clone https://github.com/USUARI/my_site.git

cd my_site
```

---

## Crear Entorn Virtual

### Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Instal·lar Dependències

```bash
pip install -r requirements.txt
```

---

# Configuració de la Base de Dades

## Executar Migracions

```bash
python manage.py migrate
```

---

## Crear Superusuari

```bash
python manage.py createsuperuser
```

---

# Executar el Projecte

## Iniciar Servidor Django

```bash
python manage.py runserver
```

---

## Accedir a l'Aplicació

```text
http://127.0.0.1:8000/
```

---

# Rutes Principals

| Ruta | Descripció |
|---|---|
| `/` | Pàgina principal |
| `/posts` | Totes les publicacions |
| `/authors` | Llista d'autors |
| `/tags` | Llista d'etiquetes |
| `/admin` | Panell administració Django |

---

# Documentació Pydoc

Aquest projecte genera documentació HTML automàtica utilitzant Pydoc.

## Generar Documentació Manualment

```bash
pydoc -w blog.views
pydoc -w blog.models
pydoc -w blog.urls
```

---

# GitHub Actions

El projecte incorpora GitHub Actions per automatitzar:

- Instal·lació de dependències
- Generació de documentació
- Publicació amb GitHub Pages
- Integració contínua

---

# GitHub Pages

La documentació generada es publica automàticament a:

```text
https://USUARI.github.io/my_site/
```

---

# Captures de Pantalla

## Pàgina Principal

<img width="1908" height="916" alt="image" src="https://github.com/user-attachments/assets/2bbfa18c-3797-4580-aeea-b56f971bd13d" />

---

## Pàgina de Publicacions

<img width="1906" height="920" alt="image" src="https://github.com/user-attachments/assets/bbc58c1a-fe50-41de-a419-bb2a290c3335" />

---

## Detall de Publicació

<img width="1907" height="917" alt="image" src="https://github.com/user-attachments/assets/24936601-ffdc-4536-be80-c09a1b457b1b" />

---

## Panell d'Administració Django

<img width="1920" height="920" alt="image" src="https://github.com/user-attachments/assets/49ba19e6-dc04-417c-b707-76b5683550c0" />

---

# Llicència

MIT License

---

# Autor

Copyright (c) 2025-2026 Toni Canal
