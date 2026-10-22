# Python Task Management

FastAPI practice project with PostgreSQL connection, SQLAlchemy models, and Alembic migrations.

## What's done so far

- FastAPI app with task/post routes (`src/main.py`)
- Pydantic schemas: `PostCreate`, `PostResponse` (`src/schema/post.py`)
- SQLAlchemy model: `Post` → table `posts` (`src/model/post.py`)
- PostgreSQL connection via `.env` (`src/database.py`)
- DB connection test script (`test.py`) — working
- Alembic setup (`alembic.ini`, `migrations/`)
- Migration created: `migrations/versions/f9624c442364_add_post_table.py`

## Not done yet

- API routes still use an **in-memory** `tasks` list
- Routes are not yet wired to PostgreSQL (`get_db` + `Post` model)

## Project structure

```
python_project/
├── app.py                 # Uvicorn entrypoint
├── test.py                # DB connection test
├── .env                   # Postgres + ImageKit credentials (not committed)
├── alembic.ini
├── pyproject.toml
├── migrations/
│   ├── env.py
│   └── versions/          # migration files
└── src/
    ├── main.py            # FastAPI routes
    ├── database.py        # engine, session, get_db
    ├── model/post.py      # SQLAlchemy Post model
    └── schema/post.py     # Pydantic schemas
```

## Requirements

- Python 3.9+
- PostgreSQL running locally
- `uv` or a venv with project dependencies

## Setup

### 1. Clone & enter project

```bash
cd python_project
```

### 2. Create virtualenv & install deps

```bash
# if using uv
uv sync

# or activate existing venv
source .venv/bin/activate
```

### 3. Configure `.env`

Create/update `.env` in project root:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=python_practice
POSTGRES_SSL=false
```

### 4. Create Postgres database (once)

```bash
createdb python_practice
# or via psql:
# CREATE DATABASE python_practice;
```

### 5. Run migrations (create tables)

```bash
alembic upgrade head
```

### 6. Test DB connection

```bash
python3 test.py
```

Expected:

```
Database connected successfully
PostgreSQL ...
```

## Run the API

```bash
python3 app.py
```

Server starts at: [http://127.0.0.1:8080](http://127.0.0.1:8080)

- Swagger docs: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- ReDoc: [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

## Current API endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/get-all-posts?limit=10` | List posts (memory) |
| `GET` | `/get-single-post/{id}` | Get one post (memory) |
| `POST` | `/add-to-tasks` | Create post (memory) |

`POST` body example:

```json
{
  "title": "Learn PostgreSQL",
  "description": "Connect FastAPI to Postgres"
}
```

## Useful commands

```bash
# new migration after model change
alembic revision --autogenerate -m "describe change"

# apply migrations
alembic upgrade head

# check posts table
psql -U your_user -d python_practice -c '\d posts'
```

## Next step

Wire `src/main.py` routes to PostgreSQL using `Depends(get_db)` and the `Post` model instead of the in-memory `tasks` list.
