import dataclasses


@dataclasses.dataclass
class Answer:
    data: str
    is_correct: bool
