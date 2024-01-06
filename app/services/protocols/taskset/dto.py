import typing


class TaskSetDTO(typing.Protocol):
    id: int | None
    name: str
