# DJA02 Advanced Social Media Application

A Django-based social media application implementing the **DJA02 Advanced Social Media Application BRD**. The project extends a basic social media app with post filtering, sorting, user filtering, keyword search, image uploads, authentication, and ownership-based post management.

## Repository name

**`dja02-advanced-social-media`**

## Features

- Django built-in authentication
- Registration, login and logout
- Global social feed
- User profile pages with only that user's posts
- Create posts with text and optional image
- Edit/delete only your own posts
- Filter by latest/oldest
- Filter by text-only/image posts
- Filter posts by user
- Keyword search using `icontains`
- Django admin for post management
- Responsive server-rendered UI

## Setup (Pipenv)

```bash
git clone <your-repository-url>
cd dja02-advanced-social-media
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Main routes

| Route | Purpose |
|---|---|
| `/` | Global feed + filters/search |
| `/register/` | Registration |
| `/login/` | Login |
| `/logout/` | Logout |
| `/profile/<username>/` | User-specific posts |
| `/posts/create/` | Create post |
| `/posts/<id>/edit/` | Edit own post |
| `/posts/<id>/delete/` | Delete own post |
| `/admin/` | Django admin |

## Query parameters

Examples:

```text
/?sort=latest
/?sort=oldest
/?media=text
/?media=image
/?user=2
/?search=django
/?search=django&media=image&sort=latest
```

## BRD coverage

- User Management: implemented
- Post Management: implemented
- Date filtering/sorting: implemented
- Media type filtering: implemented
- User filtering: implemented
- Keyword search: implemented
- Access control: implemented
- Optional image upload: implemented

## Production notes

Before deployment, move `SECRET_KEY` to environment variables, set `DEBUG=False`, configure `ALLOWED_HOSTS`, use a production database, and configure persistent media/static storage.
