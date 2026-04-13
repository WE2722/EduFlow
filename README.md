# EduFlow - Smart Student Management System

EduFlow is a production-oriented Django platform for student operations with role-based access, analytics dashboard, and REST APIs.

## Features

- Modular architecture: accounts, students, filieres, dashboard, api, core
- Custom user model with roles: Admin, Staff, Viewer
- Student lifecycle management with service-layer business logic
- Smart search with AJAX
- Analytics dashboard with Chart.js
- DRF APIs with versioning (`/api/v1/`), filtering, pagination
- OpenAPI/Swagger docs (`/api/docs/`)
- Environment-based configuration and production toggles

## Documentation

- User guide: [USER_GUIDE.md](USER_GUIDE.md)
- API docs (runtime): `/api/docs/`

## Architecture

```text
eduflow/
|-- accounts/
|-- students/
|-- filieres/
|-- dashboard/
|-- api/
|-- core/
|-- templates/
|-- static/
```

## Quick Start

1. Create and activate virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Copy env file:
   - `copy .env.example .env` (Windows)
4. Run migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
5. Create superuser:
   - `python manage.py createsuperuser`
6. Start server:
   - `python manage.py runserver`

## How To Launch The App (Detailed)

### Option 1: Local (SQLite)

1. Create virtual environment:
   - `python -m venv .venv`
2. Activate virtual environment (Windows PowerShell):
   - `.venv\Scripts\Activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Prepare environment:
   - `copy .env.example .env`
5. Ensure `.env` contains:
   - `DJANGO_DEBUG=true`
   - `DB_ENGINE=django.db.backends.sqlite3`
   - `DB_NAME=db.sqlite3`
6. Apply migrations:
   - `python manage.py makemigrations`
   - `python manage.py migrate`
7. Create admin user:
   - `python manage.py createsuperuser`
8. Optional demo data:
   - `python manage.py seed_demo_data`
9. Run app:
   - `python manage.py runserver`
10. Open:
   - App: `http://127.0.0.1:8000/`
   - Login: `http://127.0.0.1:8000/login/`
   - Dashboard: `http://127.0.0.1:8000/dashboard/`
   - Admin: `http://127.0.0.1:8000/admin/`
   - Swagger: `http://127.0.0.1:8000/api/docs/`

### Option 2: Docker + PostgreSQL

1. Ensure Docker Desktop is running.
2. Build and run:
   - `docker compose up --build`
3. In another terminal, migrate:
   - `docker compose exec web python manage.py migrate`
4. Create superuser:
   - `docker compose exec web python manage.py createsuperuser`
5. Optional demo data:
   - `docker compose exec web python manage.py seed_demo_data`
6. Open:
   - `http://127.0.0.1:8000/`

## API

- Students: `/api/v1/students/`
- Filieres: `/api/v1/filieres/`
- Dashboard: `/api/v1/dashboard/`
- Schema: `/api/schema/`
- Swagger UI: `/api/docs/`

## Demo Users (if seeded)

- Admin: `admin` / `admin12345`
- Staff: `staff` / `staff12345`
- Viewer: `viewer` / `viewer12345`

## Security and Production Notes

- Set `DJANGO_DEBUG=false` in production.
- Set a strong `DJANGO_SECRET_KEY`.
- Configure PostgreSQL via `DB_*` variables.
- Use a production WSGI/ASGI server and secure reverse proxy.

## Testing

Run:
- `python manage.py test`

## CI

GitHub Actions pipeline is provided in `.github/workflows/ci.yml`.
It installs dependencies, runs migrations, and executes the test suite on each push/PR to `main`.
