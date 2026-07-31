# Event Management Backend

A RESTful Event Management API built with Flask, SQLAlchemy, SQLite, and JWT authentication.

## Features

- User registration and login
- JWT-based authentication
- Event management CRUD operations
- Category management CRUD operations
- Database migrations with Flask-Migrate
- Secure protected routes

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Alembic / Flask-Migrate

## Project Structure

```text
event-management-backend/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── seed.py
│
├── migrations/
├── instance/
├── run.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>

cd event-management-backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
JWT_SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///event_management.db
```

## Running the Application

Start Flask:

```bash
python run.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## Authentication

### Register User

**POST**

```text
/register
```

Example request:

```json
{
    "full_name": "Test User",
    "email": "test@example.com",
    "password": "password123"
}
```

### Login

**POST**

```text
/login
```

Example response:

```json
{
    "access_token": "your_jwt_token"
}
```

Use the token for protected routes:

```text
Authorization: Bearer <token>
```

# API Endpoints

## Events

| Method | Endpoint | Authentication |
|---|---|---|
| GET | `/events` | No |
| GET | `/events/<id>` | No |
| POST | `/events` | Yes |
| PUT | `/events/<id>` | Yes |
| DELETE | `/events/<id>` | Yes |

## Categories

| Method | Endpoint | Authentication |
|---|---|---|
| GET | `/categories` | No |
| POST | `/categories` | Yes |
| PUT | `/categories/<id>` | Yes |
| DELETE | `/categories/<id>` | Yes |

## Database

Apply migrations:

```bash
flask db upgrade
```

Seed sample data:

```bash
python -m app.seed
```

## Testing

API endpoints can be tested using Postman.

Recommended testing order:

1. Register user
2. Login and obtain JWT token
3. Create category/event
4. Update category/event
5. Delete category/event
6. Verify GET endpoints

## License

This project is licensed under the MIT License.