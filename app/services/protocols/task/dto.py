import typing
from app.services.protocols.answer import AnswerDTO


class TaskDTO(typing.Protocol):
    id: int | None
    level: int
    description: str
    img: bytes | None
    answers: list[AnswerDTO]
    theme_ids: list[int]
