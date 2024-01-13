import typing

import fastapi
import pydantic

from app.web import ioc
from app import entities


class TaskDTO(pydantic.BaseModel):
    taskset_id: int | None
    level: int
    description: str
    theme_ids: list[int]


task_router = fastapi.APIRouter(prefix="/tasks", tags=["tasks"])


@task_router.get("/")
def get_task_list(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
) -> list[entities.Task]:
    with container.get_task_list() as get_task_list:
        return get_task_list()


@task_router.get("/{task_id}")
def get_task_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    task_id: int,
) -> entities.Task:
    with container.get_task_by_id() as get_task_by_id:
        return get_task_by_id(task_id)


@task_router.delete("/{task_id}")
def delete_task_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    task_id: int,
):
    with container.delete_task_by_id() as delete_task_by_id:
        return delete_task_by_id(task_id)


@task_router.post("/")
def create_task(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    task_dto: TaskDTO,
) -> entities.Task:
    with container.create_task() as create_task:
        return create_task(task_dto)
