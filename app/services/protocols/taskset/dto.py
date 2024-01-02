import typing


class TaskSetDTO(typing.Protocol):
    id: int | None
    task_ids: list[int]
