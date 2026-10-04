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
