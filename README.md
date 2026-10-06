# Recipe API

A Python API built with Django and Django REST Framework, with JWT authentication, recipes, categories, reviews, and recipe search. This repository demonstrates backend API development and integrations with Swagger documentation.

## Features

- User registration and JWT access/refresh tokens
- Recipe creation, listing, updates, and deletion
- Categories and recipe reviews
- Search by title, category name, and ingredients
- Swagger and ReDoc API documentation
- SQLite for local development

## Local setup

Use Python 3.10+ for the pinned Django 5.0.6 dependency.

```sh
git clone https://github.com/rajinder-mohan/recipe.git
cd recipe
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/swagger/ or http://127.0.0.1:8000/redoc/ for interactive API documentation. The Django project package is named `receipe`; the API application is `recipesapp`.

## Authentication

Register with `POST /api/signup/`, supplying `email`, `first_name`, `last_name`, `password`, and matching `password2`. Passwords must pass Django password validation.

Registration stores the email address as the Django username. The standard Simple JWT token endpoint expects `username`, not `email`:

```sh
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"user@example.com","password":"your-password"}'
```

Send the returned access token as `Authorization: Bearer <access-token>`. Refresh it through `POST /api/token/refresh/` with the `refresh` token.

## API routes

- `POST /api/signup/`: register
- `POST /api/token/` and `POST /api/token/refresh/`: obtain/refresh tokens
- `GET/POST /api/recipes/`: list/create recipes
- `GET/PUT/DELETE /api/recipes/{id}/`: recipe detail/update/delete
- `GET/POST /api/categories/`: list/create categories
- `GET/PUT/DELETE /api/categories/{id}/`: category detail/update/delete
- `GET/POST /api/reviews/`: list/create reviews
- `GET/PUT/DELETE /api/reviews/{id}/`: review detail/update/delete
- `GET /api/search/?title=&category=&ingredients=`: search recipes

Create a category with `{"name":"Dinner"}` and use its returned ID when creating a recipe. Recipe fields are `title`, `description`, `ingredients`, `preparation_steps`, `cooking_time` (minutes), `serving_size`, and `category`.

Category routes require authentication. Recipe and review writes require authentication, and detail operations currently filter to the signed-in user's records. Search and recipe/review list routes permit anonymous reads.

## Development checks

```sh
python manage.py check
python manage.py test
```

The current `recipesapp/tests.py` is a scaffold with no implemented tests. Passing the test command does not yet demonstrate API test coverage.

## Deployment status

The checked-in settings are for local development: debug mode is enabled, hosts are unrestricted, and the signing key is a development value. Configure production settings and a private signing key before deployment. This README does not claim production readiness or automated test coverage.
