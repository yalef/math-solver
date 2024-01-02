import dataclasses
from .answer import Answer
from .theme import Theme


@dataclasses.dataclass
class Task:
    answers: list[Answer]
    themes: list[Theme]
    level: int
    description: str
    img: bytes | None
