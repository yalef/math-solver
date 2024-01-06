import app.entities
from app.services import protocols


class TaskSetGateway(protocols.TaskSetReader, protocols.TaskSetSaver):
    pass


class TaskSetSolver:
    def __init__(
        self,
        uow: protocols.UoW,
        task_gateway: protocols.TaskReader,
        taskset_gateway: TaskSetGateway,
    ):
        self._uow = uow
        self._task_gateway = task_gateway
        self._taskset_gateway = taskset_gateway

    def __call__(
        self,
        taskset_id: int,
        task_id: int,
        answer_dto: protocols.AnswerDTO,
    ) -> app.entities.TaskSet:
        answer = app.entities.Answer(
            id=answer_dto.id,
            data=answer_dto.data,
            is_correct=answer_dto.is_correct,
        )
        task: app.entities.Task = self._task_gateway.get_task_by_id(task_id)
        # taskset.solve_task(task, answer)
        task.solve(answer)
        self._task_gateway.save(task)
        taskset: app.entities.TaskSet = self._taskset_gateway.get_taskset_by_id(
            taskset_id
        )
        self._uow.commit()
        return taskset
