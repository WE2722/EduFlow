# EduFlow User Guide

## 1. What EduFlow Is

EduFlow is a smart student management platform designed for academic teams.
It centralizes student records, filieres (programs), analytics, and APIs.

## 2. User Roles

- Admin:
  - Full platform access
  - Can create/update/delete students and filieres
  - Access to admin panel and all API write operations
- Staff:
  - Can create/update/delete students via web and API
  - Can access dashboard and student pages
- Viewer:
  - Read-only access to pages and API safe endpoints

## 3. Main Pages

- Login: `/login/`
- Dashboard: `/dashboard/`
- Students list: `/students/`
- Add student: `/students/add/`
- Admin back-office: `/admin/`
- API docs (Swagger): `/api/docs/`

## 4. Students Module

### 4.1 Student List

The students list page includes:
- Search by first name, last name, email, phone
- Filters by filiere and status
- Pagination
- CSV export

### 4.2 Smart Search (AJAX)

While typing in the search box, EduFlow fetches matching students and displays a quick result list without page reload.

### 4.3 Student Profile

Each student has a full detail page containing:
- Personal info
- Filiere
- Status
- Photo
- Audit metadata (created by / updated by)

### 4.4 CRUD Actions

- Create: add a new student
- Update: edit student profile
- Delete: remove student with confirmation
- Export: download CSV list

## 5. Filiere Module

Filieres are normalized entities with:
- Code (unique)
- Name (unique)
- Description
- Active flag

Students are linked to filieres through a ForeignKey relation.

## 6. Dashboard & Analytics

Dashboard includes:
- Total students
- Students per filiere
- Status distribution
- Recent activity

Charts are rendered with Chart.js.

## 7. API Usage

Base versioned prefix: `/api/v1/`

Endpoints:
- `GET/POST /api/v1/students/`
- `GET/POST /api/v1/filieres/`
- `GET /api/v1/dashboard/`

Features:
- Pagination
- Search
- Filtering
- Ordering
- Role-aware write permissions

## 8. API Docs

- OpenAPI schema: `/api/schema/`
- Swagger UI: `/api/docs/`

Use Swagger UI to test endpoints interactively.

## 9. Notifications & Messages

The web UI shows contextual alerts for:
- Successful create/update/delete operations
- Permission denials
- Validation errors

## 10. Security Notes

- Protected routes require authentication
- Mutating actions are role-restricted
- Environment variables are used for secret and DB settings
- Keep `DJANGO_DEBUG=false` in production

## 11. Typical Workflow

1. Login
2. Open Dashboard
3. Review metrics
4. Manage filieres and students
5. Search/filter students
6. Export CSV when needed
7. Use API for integrations

## 12. Troubleshooting

- Migration issues:
  - Run `python manage.py makemigrations`
  - Run `python manage.py migrate`
- Missing static/media in production:
  - Run `python manage.py collectstatic`
  - Configure web server static/media mapping
- Permission denied on actions:
  - Verify your user role (Admin or Staff for write operations)
