# 🌍 Wanderlust

Wanderlust is a travel blog creation app built with Django. Write, publish, and
share your travel stories in one place.

## ✨ Features

- Create, edit, and delete travel blog posts
- Browse posts from other travelers
- Django admin panel for managing content
- <!-- Add: user accounts, image uploads, comments, categories, etc. -->

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Config:** python-dotenv / environment variables via `.env`
- **Static files:** Django `staticfiles` (`collectstatic`)

## 📁 Project Structure

```
wanderlust/
├── blog/             # Main app: models, views, templates, URLs
├── wanderlust/       # Project settings, URLs, WSGI/ASGI config
├── staticfiles/      # Collected static assets (generated)
├── manage.py
├── requirements.txt
└── .env.example      # Template for environment variables
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<username>/wanderlust.git
   cd wanderlust
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root (next to `manage.py`):
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create an admin user (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files (needed for production)**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/ to see the app, or http://127.0.0.1:8000/admin/
for the admin panel.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push and open a pull request

## 📄 License

<!-- Add a license, e.g. MIT -->

## 👥 Authors

Group_Hurricane