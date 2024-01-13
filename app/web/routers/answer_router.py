import typing

import fastapi
import pydantic

from app.web import ioc
from app import entities


class AnswerDTO(pydantic.BaseModel):
    data: str
    is_correct: bool
    task_id: int | None


answer_router = fastapi.APIRouter(prefix="/answers", tags=["answers"])


@answer_router.get("/")
def get_answer_list(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
) -> list[entities.Answer]:
    with container.get_answer_list() as get_answer_list:
        return get_answer_list()


@answer_router.get("/{answer_id}")
def get_answer_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    answer_id: int,
) -> entities.Answer:
    with container.get_answer_by_id() as get_answer_by_id:
        return get_answer_by_id(answer_id)


@answer_router.delete("/{answer_id}")
def delete_answer_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    answer_id: int,
) -> None:
    with container.delete_answer_by_id() as delete_answer_by_id:
        return delete_answer_by_id(answer_id)


@answer_router.post("/")
def create_answer(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    answer_dto: AnswerDTO,
) -> entities.Answer:
    with container.create_answer() as create_answer:
        return create_answer(answer_dto)
