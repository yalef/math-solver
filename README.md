# About
This project is part of an application that generates math problems and provides api to solve them.
It is backend service for creating, solving and storing math problems.

# Main entities
- **Task** - one instance of task. Keep detail information of math problem.
- **TaskSet** - set of tasks, has unique name and can be assigned to some student.
- **Theme** - theme which can be related to some tasks.
- **Answer** - task can have several answers, some of them can be true, some of them false. Task always should have one true answer

# Project structure
There're several layers:
- **entities** - inner entities, which contain main business logic
- **services** - service layer, contains business logic and interactions with data storage
- **adapters** - contains adapters to external data (external api, database etc.)
- **web** - contains web framework routers and calls functions from service layer.
- **main** - entrypoint to app, contains app builder and IoC container implementation.

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
