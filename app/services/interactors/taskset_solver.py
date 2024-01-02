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
            data=answer_dto.data,
            is_correct=answer_dto.is_correct,
        )
        task: app.entities.Task = self._task_gateway.get_task_by_id(task_id)
        taskset: app.entities.TaskSet = self._taskset_gateway.get_taskset_by_id(
            taskset_id
        )
        taskset.solve_task(task, answer)
        self._taskset_gateway.save(taskset)
        self._uow.commit()
        return taskset
