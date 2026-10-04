
### Advanced Social Media Application

A Django-based social media application implementing the **DJA0 & DJA02 Advanced Social Media Application BRD**. The project extends a basic social media app with post filtering, sorting, user filtering, keyword search, image uploads, authentication, and ownership-based post management.

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
=======
# DJA02 - Advanced Social Media Application

A Django-based social media application developed as part of the **DJA02 Advanced Social Media Application BRD** assignment.

This project extends a basic social media application with advanced **post filtering, sorting, user-based filtering, and keyword search** functionality.

---

## Features

### User Authentication
- User registration
- User login and logout
- Django's built-in authentication system
- Authentication-protected post operations

### Post Management
- Create posts with text content
- Optional image upload
- View all posts on the homepage
- View posts from a specific user
- Edit your own posts
- Delete your own posts
- Users cannot edit or delete other users' posts

### Post Filtering & Search
- Sort posts by:
  - Latest
  - Oldest
- Filter posts by media type:
  - Text-only
  - Image posts
  - All posts
- Filter posts by specific user
- Search posts by keywords in their content
- Combine multiple filters and search parameters

---

## Tech Stack

- **Backend:** Django
- **Database:** SQLite
- **Authentication:** Django Authentication
- **Frontend:** Django Templates, HTML, CSS
- **Image Handling:** Pillow
- **Package Management:** Pipenv
- **Language:** Python 3.13

---

## Project Structure

```text
dja02-advanced-social-media/
│
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
│
├── social_media/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── registration/
│
└── media/
>>>>>>> 3c50897af4ac8c371ae6fce1e1b419a78deb9a02
