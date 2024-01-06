import dataclasses


@dataclasses.dataclass
class Answer:
    data: str
    is_correct: bool
    id: int | None = None
    task_id: int | None = None
