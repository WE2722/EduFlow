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

## API

- Students: `/api/v1/students/`
- Filieres: `/api/v1/filieres/`
- Dashboard: `/api/v1/dashboard/`
- Schema: `/api/schema/`
- Swagger UI: `/api/docs/`

## Security and Production Notes

- Set `DJANGO_DEBUG=false` in production.
- Set a strong `DJANGO_SECRET_KEY`.
- Configure PostgreSQL via `DB_*` variables.
- Use a production WSGI/ASGI server and secure reverse proxy.

## Testing

Run:
- `python manage.py test`
