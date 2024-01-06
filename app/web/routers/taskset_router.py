import typing

import fastapi
import pydantic

from app.services.interactors import taskset_solver
from app.web import ioc


class TaskSetDTO(pydantic.BaseModel):
    name: str


class AnswerDTO(pydantic.BaseModel):
    data: str
    is_correct: bool


taskset_router = fastapi.APIRouter(prefix="/tasksets", tags=["tasksets"])


@taskset_router.get("/")
def get_taskset_list(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
):
    with container.get_taskset_list() as get_taskset_list:
        return get_taskset_list()


@taskset_router.get("/{taskset_id}")
def get_taskset_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    taskset_id: int,
):
    with container.get_taskset_by_id() as get_taskset_by_id:
        return get_taskset_by_id(taskset_id)


@taskset_router.delete("/{taskset_id}")
def delete_taskset_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    taskset_id: int,
):
    with container.delete_taskset_by_id() as delete_taskset_by_id:
        return delete_taskset_by_id(taskset_id)


@taskset_router.post("/")
def create_taskset(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    taskset_dto: TaskSetDTO,
):
    with container.create_taskset() as create_taskset:
        return create_taskset(taskset_dto)


@taskset_router.post("/solve")
def solve_task(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    solve_dto: taskset_solver.SolveDTO,
):
    with container.solve_task() as solve_task:
        return solve_task(
            solve_dto=solve_dto,
        )
