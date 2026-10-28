# Python Practice API

FastAPI backend with PostgreSQL, SQLAlchemy, Alembic migrations, JWT auth, and a layered (router → service → model) structure.

## Features

- User registration & login with Argon2 password hashing
- JWT access tokens (`HTTPBearer` — paste token in Swagger Authorize)
- Protected routes via `get_current_user` dependency
- Posts CRUD with pagination
- Alembic migrations for schema changes

## Project structure

```
python_project/
├── app.py                      # Uvicorn entrypoint
├── test.py                     # DB connection smoke test
├── .env                        # secrets (not committed)
├── alembic.ini
├── pyproject.toml
├── migrations/
│   ├── env.py
│   └── versions/
└── src/
    ├── main.py                 # FastAPI app + router mounts
    ├── database.py             # engine, session, get_db
    ├── dependencies/
    │   └── auth.py             # get_current_user (HTTPBearer)
    ├── routers/
    │   ├── auth.py             # /auth/login
    │   ├── user.py             # /users register + /me
    │   └── post.py             # /posts CRUD
    ├── services/               # business logic
    ├── model/                  # SQLAlchemy models (User, Post)
    ├── schema/                 # Pydantic request/response schemas
    └── utils/
        ├── hash_password.py
        └── token.py            # JWT create / verify
```

## Requirements

- Python 3.9+
- PostgreSQL running locally
- `uv` (recommended) or a venv with project deps

## Setup

### 1. Enter project

```bash
cd python_project
```

### 2. Install dependencies

```bash
uv sync
# or: source .venv/bin/activate && pip install -e .
```

### 3. Configure `.env`

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=python_practice

SECRET_KEY=your-long-random-secret
ALGORITHM=HS256
TOKEN_EXPIRE_TIME=60
```

`TOKEN_EXPIRE_TIME` is in **minutes**.

### 4. Create database (once)

```bash
createdb python_practice
```

### 5. Run migrations

```bash
alembic upgrade head
```

### 6. (Optional) Test DB connection

```bash
python3 test.py
```

## Run the API

```bash
python3 app.py
```

- API: [http://127.0.0.1:8080](http://127.0.0.1:8080)
- Swagger: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- ReDoc: [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

## Auth flow (Swagger)

1. `POST /users/` — register (returns `access_token`)
2. Or `POST /auth/login` with JSON:

```json
{
  "email": "you@example.com",
  "password": "yourpassword"
}
```

3. Copy `access_token` from the response
4. Click **Authorize** in Swagger → paste token only (no `Bearer ` prefix)
5. Call protected routes (e.g. `GET /users/me`)

## API endpoints

### Auth

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/auth/login` | No | Login, returns JWT |

### Users

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/users/` | No | Register user |
| `GET` | `/users/me` | Yes | Current user from token |

### Posts

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/posts/?page=1&limit=10` | No | List posts (paginated) |
| `POST` | `/posts/` | No* | Create post |
| `PUT` | `/posts/?id={id}` | No* | Update post |
| `DELETE` | `/posts/?id={id}` | No* | Delete post |

\* Posts write routes are not yet protected; wire `Depends(get_current_user)` when ready.

**Register body:**

```json
{
  "userName": "daniyal",
  "email": "daniyal@gmail.com",
  "phone_number": "+923001234567",
  "password": "secret123"
}
```

**Create post body:**

```json
{
  "title": "Learn FastAPI auth",
  "description": "JWT + HTTPBearer dependency"
}
```

## Useful commands

```bash
# new migration after model change
alembic revision --autogenerate -m "describe change"

# apply migrations
alembic upgrade head

# inspect tables
psql -U your_user -d python_practice -c '\dt'
```

## Stack

| Layer | Tech |
|-------|------|
| API | FastAPI + Uvicorn |
| DB | PostgreSQL + SQLAlchemy + psycopg |
| Migrations | Alembic |
| Auth | PyJWT + HTTPBearer |
| Passwords | pwdlib (Argon2) |
| Validation | Pydantic v2 |
