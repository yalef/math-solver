import dataclasses

from .task import Task, TaskStatus


@dataclasses.dataclass
class TaskSet:
    id: int | None
    name: str
    tasks: list[Task]

    @property
    def is_solved(self) -> bool:
        completed_statuses = [TaskStatus.completed, TaskStatus.failed]
        return all([task.status in completed_statuses for task in self.tasks])
