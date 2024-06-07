# Recipe API Project

This project is a Recipe API built using Django and Django REST Framework (DRF). It allows users to perform CRUD operations on recipes, authenticate using JWT, and search for recipes based on various criteria.

## Features

- User authentication and authorization using JWT.
- CRUD operations on recipes (Create, Read, Update, Delete).
- Recipe details including title, description, ingredients, preparation steps, cooking time, and serving size.
- Categorization of recipes into different categories.
- Search and filter recipes based on title, category, and ingredients.
- Swagger documentation for API endpoints.

## Requirements

- Python 3.8+

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/recipe-api.git
    cd recipe-api
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the API documentation:**

    Open your browser and navigate to `http://127.0.0.1:8000/swagger/` for Swagger UI or `http://127.0.0.1:8000/redoc/` for Redoc.

## Usage

### Endpoints

- **User Registration:** `POST /api/signup/`
- **Token Obtain Pair:** `POST /api/token/`
- **Token Refresh:** `POST /api/token/refresh/`
- **Recipe List/Create:** `GET/POST /api/recipes/`
- **Recipe Detail/Update/Delete:** `GET/PUT/DELETE /api/recipes/{id}/`
- **Category List:** `GET /api/categories/`
- **Review List/Create:** `GET/POST /api/reviews/`
- **Review Detail/Update/Delete:** `GET/PUT/DELETE /api/reviews/{id}/`
- **Recipe Search:** `GET /api/search/?title=&category=&ingredients=`

### Example Requests

- **User Registration:**

    ```json
    POST /api/signup/
    {
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "yourpassword",
        "password2": "yourpassword"
    }
    ```

- **Token Obtain Pair:**

    ```json
    POST /api/token/
    {
        "email": "user@example.com",
        "password": "yourpassword"
    }
    ```

- **Create Recipe:**

    ```json
    POST /api/recipes/
    {
        "title": "Biryani",
        "description": "Rice dish veg and non veg",
        "ingredients": "Rice, chicken, salt, cinnamon, custard",
        "preparation_steps": "boil rice. mix curd with vegetables and chicken then cook in handi",
        "cooking_time": 60,
        "serving_size": 2,
        "category": 2
    }
    ```
