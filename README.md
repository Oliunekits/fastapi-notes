# FastAPI Notes API

A simple Notes REST API built with FastAPI and SQLAlchemy.

This project is created as a portfolio example for a Junior Python Developer.

It demonstrates:

- Clean project structure (routers, services, repositories, models)
- CRUD operations for notes
- Text search and filter by tag
- Database layer with SQLAlchemy and SQLite
- Typing and validation with Pydantic

---

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic, pydantic-settings
- SQLite (local file `notes.db`)

---

## Project Structure

```text
fastapi-notes/
    app/
        api/
            __init__.py
            notes.py          # API routes for notes
            router.py         # main API router
        core/
            __init__.py
            config.py         # application settings (DATABASE_URL)
        db/
            __init__.py
            database.py       # engine, SessionLocal, Base
        models/
            __init__.py
            note.py           # SQLAlchemy Note model
        repositories/
            __init__.py
            notes_repository.py  # database access layer
        schemas/
            __init__.py
            note.py           # Pydantic schemas
        services/
            __init__.py
            notes_service.py  # business logic
        main.py               # FastAPI application
    .env                      # environment variables (optional)
    requirements.txt

## Installation and Run (local)

Clone the repository

git clone https://github.com/oliunekits/fastapi-notes.git
cd fastapi-notes


Create and activate a virtual environment

python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the application

uvicorn app.main:app --reload


Open in browser

Swagger UI: http://127.0.0.1:8000/docs

Notes endpoints: http://127.0.0.1:8000/api/notes/

Database tables are created automatically on application startup.

## API Endpoints

Base prefix: /api/notes/

List notes
GET /api/notes/


## Query parameters:

q – search in title or content (optional)

tag – filter by tag substring (optional)

## Get note by id
GET /api/notes/{note_id}

## Create note
POST /api/notes/
Content-Type: application/json

{
  "title": "My first note",
  "content": "Some text here",
  "tags": "study,python"
}

## Update note
PUT /api/notes/{note_id}
Content-Type: application/json

{
  "title": "Updated title",
  "content": "Updated content",
  "tags": "updated,tag"
}

## Delete note
DELETE /api/notes/{note_id}

Author

orest oliunekits
Junior Python Developer
GitHub: https://github.com/oliunekits
