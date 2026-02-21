# User CRUD API (Django REST Framework)

A simple scalable and well-structured User CRUD API built with Django and Django REST Framework.

This project demonstrates backend fundamentals including validation, pagination, filtering, ordering, and role-based permissions.

# Features

Create, Read, Update, Delete Users

Pagination

Age Validation (18+ restriction)

Duplicate Prevention (unique username & email)

Filtering by age and username

Search functionality

Ordering (ascending & descending)

Role-Based Permissions (Admin vs Regular User)

# Tech Stack

Python

Django

Django REST Framework

SQLite (default database)

django-filter

# API Endpoints

Base URL:

/api/users/
Example Requests

Get all users (paginated)

GET /api/users/

Filter users

GET /api/users/?age=22

Search users

GET /api/users/?search=emma

Order users

GET /api/users/?ordering=-age

Create user

POST /api/users/

Delete user (Admin only)

DELETE /api/users/{id}/
# Permissions

Authenticated users can view users.

Only Admin users can create, update, or delete users.

Age must be 18 or older.

Username and Email must be unique.

# How to Run Locally

Clone the repository

git clone https://github.com/yourusername/repo-name.git

Navigate into project folder

cd repo-name

Create virtual environment

python -m venv venv

Activate virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Start server

python manage.py runserver

# Project Growth

This project is continuously being improved to deepen backend engineering understanding. Future improvements may include:

Relationships (User → Posts)

Soft delete functionality

Automated testing

Deployment

# Author

Built as part of a backend development learning journey focused on building scalable and secure APIs.
