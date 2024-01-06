import dataclasses

import app.entities
from app.services import protocols


@dataclasses.dataclass
class TaskSetResultDTO:
    id: int
    tasks: list[app.entities.Task]
    is_solved: bool


@dataclasses.dataclass
class SolveDTO:
    task_id: int
    answer_id: int


class TaskSetGateway(protocols.TaskSetReader, protocols.TaskSetSaver):
    pass


class TaskSetSolver:
    def __init__(
        self,
        uow: protocols.UoW,
        task_gateway: protocols.TaskReader,
        taskset_gateway: TaskSetGateway,
        answer_gateway: protocols.AnswerReader,
    ):
        self._uow = uow
        self._task_gateway = task_gateway
        self._taskset_gateway = taskset_gateway
        self._answer_gateway = answer_gateway

    def __call__(
        self,
        solve_dto: SolveDTO,
    ) -> TaskSetResultDTO:
        answer = self._answer_gateway.get_answer_by_id(solve_dto.answer_id)
        task: app.entities.Task = self._task_gateway.get_task_by_id(
            solve_dto.task_id,
        )
        task.solve(answer)
        self._task_gateway.save(task)
        taskset: app.entities.TaskSet = self._taskset_gateway.get_taskset_by_id(
            task.taskset_id,
        )
        self._uow.commit()
        return TaskSetResultDTO(
            id=taskset.id,
            tasks=taskset.tasks,
            is_solved=taskset.is_solved,
        )
