# Installation
```bash
# init python env
poetry install
poetry shell

# run database
docker compose up -d --build
# apply migrations for database
alembic upgrade head
```
