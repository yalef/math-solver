import dataclasses
from .task import Task, TaskStatus


@dataclasses.dataclass
class TaskSet:
    id: int | None
    name: str
    tasks: list[Task]
    # solved_tasks: list[Task]
    # correction_tasks: list[Task]
    # failed_tasks: list[Task]

    # def solve_task(self, task: Task, answer: Answer):
    #     if answer in task.answers and answer.is_correct:
    #         self.solved_tasks.append(task)
    #         if task in self.tasks:
    #             self.tasks.remove(task)
    #         elif task in self.correction_tasks:
    #             self.correction_tasks.remove(task)
    #     else:
    #         if task in self.correction_tasks:
    #             self.correction_tasks.remove(task)
    #             self.failed_tasks.append(task)
    #         elif task in self.tasks:
    #             self.tasks.remove(task)
    #             self.correction_tasks.append(task)

    @property
    def is_solved(self) -> bool:
        completed_statuses = [TaskStatus.completed, TaskStatus.failed]
        return all([
            task.status in completed_statuses
            for task in self.tasks
        ])
