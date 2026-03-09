# Wanderlust 🌍

> A creative travel blog platform built with Django — share your stories, discover new places, and connect with fellow adventurers.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2.5-green?logo=django)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-CDN-38bdf8?logo=tailwindcss)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Development Server](#running-the-development-server)
- [URL Reference](#url-reference)
- [Data Models](#data-models)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Team](#team)

---

## About the Project

**Wanderlust** is a full-stack blog web application that lets users write and share travel stories. Readers can browse all published posts on the homepage, read full articles, and registered users can create, edit, or delete their own posts.

The UI features a hero landing section with an animated scroll-reveal effect, a sticky navbar that transitions from transparent to solid on scroll, a responsive card grid for post listings, and glassmorphism-style forms.

---

## Features

| Feature | Description |
|---|---|
| 🏠 Home Feed | Paginated grid of all blog posts, newest first |
| ✍️ Create Post | Authenticated users can publish new stories |
| 📖 Post Detail | Full post view with author name and publish date |
| ✏️ Edit Post | Authors can update their own posts |
| 🗑️ Delete Post | Authors can delete their own posts with confirmation |
| 🔐 Authentication | Register, login, and logout with Django's built-in auth |
| 🚫 Author Guard | Editing or deleting another user's post returns HTTP 403 |
| 📱 Responsive | Mobile-friendly navbar with hamburger menu |
| 🎨 Animated UI | Scroll-reveal cards, hover effects, gradient buttons |

---

## Tech Stack

### Backend
| Technology | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Core language |
| Django | 5.2.5 | Web framework |
| SQLite | (built-in) | Development database |
| PyMySQL | 1.1.1 | Production MySQL driver |
| Gunicorn | 23.0.0 | Production WSGI server |
| python-dotenv | 1.1.1 | Environment variable loading |

### Frontend
| Technology | Source | Purpose |
|---|---|---|
| Tailwind CSS | CDN | Utility-first CSS framework |
| Bootstrap 5 | CDN | Post-edit form styling |
| Playfair Display / Poppins | Google Fonts | Typography |
| Font Awesome 6 | CDN | Icons (logout page) |

---

## Project Structure

```
Group_Hurricane/
├── .gitignore
├── README.md
└── wanderlust/                     # Django project root
    ├── manage.py                   # Django management script
    ├── requirements.txt            # Python dependencies
    ├── .env                        # Local environment variables (not committed)
    ├── db.sqlite3                  # SQLite database (development)
    │
    ├── blog/                       # Main Django application
    │   ├── migrations/             # Database migration files
    │   ├── templates/              # App-level HTML templates
    │   │   ├── home.html           # Homepage (hero + post grid)
    │   │   ├── new_post.html       # Create-post form
    │   │   ├── post_detail.html    # Single post view
    │   │   ├── post_update.html    # Edit-post form
    │   │   └── logout.html         # Logout confirmation page
    │   ├── admin.py                # Django admin configuration
    │   ├── apps.py                 # App configuration
    │   ├── forms.py                # PostForm (ModelForm)
    │   ├── models.py               # Database models
    │   ├── tests.py                # Test suite
    │   ├── urls.py                 # App URL patterns
    │   └── views.py                # View functions
    │
    └── wanderlust/                 # Django project package
        ├── templates/              # Project-level templates
        │   ├── post_detail.html    # Standalone post detail template
        │   └── registration/
        │       ├── login.html      # Login page
        │       └── register.html   # Registration page
        ├── settings.py             # Project settings
        ├── urls.py                 # Root URL configuration
        ├── wsgi.py                 # WSGI entry point
        └── asgi.py                 # ASGI entry point
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

```bash
python --version   # should be 3.10+
pip --version
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Vineet-shukl/Group_Hurricane.git
cd Group_Hurricane
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Install dependencies**

```bash
cd wanderlust
pip install -r requirements.txt
```

4. **Apply database migrations**

```bash
python manage.py migrate
```

5. **Create a superuser** (optional — for admin panel access)

```bash
python manage.py createsuperuser
```

### Environment Variables

Create a `.env` file inside the `wanderlust/` directory (next to `manage.py`):

```dotenv
DJANGO_SECRET_KEY=your-very-secret-key-here
DEBUG=True
```

> ⚠️ **Never commit your `.env` file or expose `DJANGO_SECRET_KEY` in production.**

### Running the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

| Page | URL |
|---|---|
| Homepage | http://127.0.0.1:8000/ |
| Register | http://127.0.0.1:8000/register/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Create Post | http://127.0.0.1:8000/create/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## URL Reference

| Method | URL Pattern | View | Description |
|---|---|---|---|
| GET | `/` | `home` | Homepage — all posts ordered by newest |
| GET/POST | `/create/` | `create_post` | Create a new post (login required) |
| GET | `/post/<pk>/` | `post_detail` | View a single post |
| GET/POST | `/post/<pk>/edit/` | `post_update` | Edit a post (author only) |
| POST | `/post/<pk>/delete/` | `post_delete` | Delete a post (author only) |
| GET/POST | `/register/` | `register` | User registration |
| GET/POST | `/accounts/login/` | Django built-in | User login |
| GET | `/logout/` | `custom_logout` | Log out and show confirmation |
| — | `/admin/` | Django admin | Admin interface |

---

## Data Models

### `Post` *(active model)*

The primary model used throughout the application.

| Field | Type | Description |
|---|---|---|
| `id` | AutoField | Primary key |
| `topic` | CharField(200) | Post title / headline |
| `content` | TextField | Full post body |
| `created_at` | DateTimeField | Set automatically on creation |
| `updated_at` | DateTimeField | Updated automatically on each save |
| `author` | ForeignKey → `User` | Django's built-in `auth.User` |

### `PostForm`

A `ModelForm` backed by `Post` that exposes the `topic` and `content` fields with Tailwind CSS widget styling.

---

## Running Tests

```bash
cd wanderlust
python manage.py test blog
```

To run with verbose output:

```bash
python manage.py test blog --verbosity=2
```

---

## Deployment

The project includes Gunicorn as the production WSGI server.

1. Set `DEBUG=False` and a strong `DJANGO_SECRET_KEY` in your `.env`.
2. Collect static files:

```bash
python manage.py collectstatic
```

3. Start Gunicorn:

```bash
gunicorn wanderlust.wsgi:application --bind 0.0.0.0:8000
```

For MySQL in production, update `DATABASES` in `settings.py` to use `django.db.backends.mysql` and configure the connection credentials.

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -m "Add my new feature"`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Open a Pull Request

Please make sure `python manage.py check` reports no issues before submitting.

---

## Team

Built with ❤️ by **Team Hurricane**

&copy; 2025 Wanderlust — Group_Hurricane