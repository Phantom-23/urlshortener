# url shortener #

```markdown
# URL Shortener

A simple URL shortening service built with Django.

## Prerequisites

- Python 3.x
- Django 3.x or later

## Getting Started

Follow these steps to set up and run the URL shortener locally.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Phantom-23/urlshortener.git
cd urlshortener
```

### 2. Install Required Packages

Install the necessary Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

Before running the server, apply the database migrations:

```bash
python manage.py migrate
```

### 4. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

### 5. Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:8000
```

You should see the URL shortener application running.

## Project Structure

```
urlshortener/
│
├── manage.py             # Django's command-line utility for administrative tasks.
├── db.sqlite3            # SQLite database file.
├── requirements.txt      # A list of required Python packages.
│
├── urlshortener/         # Main application directory.
   ├── __init__.py
   ├── settings.py       # Django settings for the project.
   ├── urls.py           # URL routing for the application.
   ├── wsgi.py           # WSGI configuration for deployment.
   ├── asgi.py           # ASGI configuration for asynchronous deployment.
   |─ app/                  # Directory containing the main app.
    ├── migrations/       # Database migrations.
    ├── models.py         # Database models.
    ├── views.py          # Application views.
    ├── urls.py           # URL routing for the app.
    ├── templates/        # HTML templates.
    └── static/           # Static files (CSS, JavaScript, images).
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
