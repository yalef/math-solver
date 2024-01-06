import dataclasses
import enum

from .answer import Answer
from .theme import Theme


class TaskStatus(str, enum.Enum):
    started = "STARTED"
    correction = "CORRECTION"
    failed = "FAILED"
    completed = "COMPLETED"


@dataclasses.dataclass
class Task:
    id: int | None
    taskset_id: int
    answers: list[Answer]
    themes: list[Theme]
    level: int
    description: str
    status: TaskStatus = TaskStatus.started
    img: bytes | None = None

    def solve(self, answer: Answer):
        solvable_statuses = [TaskStatus.started, TaskStatus.correction]
        if answer in self.answers and answer.is_correct:
            if self.status in solvable_statuses:
                self.status = TaskStatus.completed
        else:
            if self.status == TaskStatus.correction:
                self.status = TaskStatus.failed
            elif self.status == TaskStatus.started:
                self.status == TaskStatus.correction
