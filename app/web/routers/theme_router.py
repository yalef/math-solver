import typing

import fastapi
import pydantic

from app.web import ioc
from app import entities


class ThemeDTO(pydantic.BaseModel):
    name: str


router = fastapi.APIRouter(prefix="/themes", tags=["themes"])


@router.get("/")
def get_theme_list(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
) -> list[entities.Theme]:
    with container.get_theme_list() as get_theme_list:
        return get_theme_list()


@router.get("/{theme_id}")
def get_theme_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    theme_id: int,
):
    with container.get_theme_by_id() as get_theme_by_id:
        return get_theme_by_id(theme_id)


@router.delete("/{theme_id}")
def delete_theme_by_id(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    theme_id: int,
):
    with container.delete_theme_by_id() as delete_theme_by_id:
        return delete_theme_by_id(theme_id)


@router.post("/")
def create_theme(
    container: typing.Annotated[ioc.InteractorFactory, fastapi.Depends()],
    theme_dto: ThemeDTO,
):
    with container.create_theme() as create_theme:
        return create_theme(theme_dto)
