import typing


class AnswerDTO(typing.Protocol):
    id: int | None
    task_id: int | None
    data: str
    is_correct: bool
