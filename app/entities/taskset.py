import dataclasses
from .task import Task
from .answer import Answer


@dataclasses.dataclass
class TaskSet:
    tasks: list[Task]
    solved_tasks: list[Task]
    correction_tasks: list[Task]
    failed_tasks: list[Task]

    def solve_task(self, task: Task, answer: Answer):
        if answer in task.answers and answer.is_correct:
            self.solved_tasks.append(task)
            if task in self.tasks:
                self.tasks.remove(task)
            elif task in self.correction_tasks:
                self.correction_tasks.remove(task)
        else:
            if task in self.correction_tasks:
                self.correction_tasks.remove(task)
                self.failed_tasks.append(task)
            elif task in self.tasks:
                self.tasks.remove(task)
                self.correction_tasks.append(task)

    @property
    def is_solved(self) -> bool:
        if len(self.tasks) == 0 and len(self.correction_tasks) == 0:
            return True
        return False
