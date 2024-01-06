import typing

import fastapi

from app.main import ioc
from app.web import ioc as ioc_protocol
from app.web import routers

DependencyT = typing.TypeVar("DependencyT")


def singleton(value: DependencyT) -> typing.Callable[[], DependencyT]:
    """Produce save value as a fastapi dependency."""

    def singleton_factory() -> DependencyT:
        return value

    return singleton_factory


def create_app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    db_url = "postgresql://postgres:postgres@localhost:5432/postgres"
    container = ioc.IoC(db_url)
    app.dependency_overrides.update(
        {
            ioc_protocol.InteractorFactory: singleton(container),
        }
    )
    app.include_router(routers.theme_router)
    app.include_router(routers.answer_router)
    app.include_router(routers.task_router)
    app.include_router(routers.taskset_router)
    return app


app = create_app()
