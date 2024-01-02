import app.entities
from app.services import protocols


class TaskSetGet:
    def __init__(
        self,
        uow: protocols.UoW,
        taskset_gateway: protocols.TaskReader,
    ):
        self._uow = uow
        self._taskset_gateway = taskset_gateway

    def __call__(self, task_id: int) -> app.entities.TaskSet:
        taskset = self._taskset_gateway.get_task_by_id(task_id)
        self._uow.commit()
        return taskset


class TaskSetCreate:
    def __init__(
        self,
        uow: protocols.UoW,
        taskset_gateway: protocols.TaskSetSaver,
        tasks_gateway: protocols.TaskReader,
    ):
        self._uow = uow
        self._taskset_gateway = taskset_gateway
        self._task_gateway = tasks_gateway

    def __call__(self, task_dto: protocols.TaskSetDTO) -> None:
        tasks = self._task_gateway.get_tasks_by_ids(task_dto.task_ids)
        taskset = app.entities.TaskSet(
            tasks=tasks,
            solved_tasks=[],
            correction_tasks=[],
            failed_tasks=[],
        )
        self._taskset_gateway.save(taskset)
        self._uow.commit()


class TaskSetDelete:
    def __init__(
        self,
        uow: protocols.UoW,
        taskset_gateway: protocols.TaskDeleter,
    ):
        self._uow = uow
        self._taskset_gateway = taskset_gateway

    def __call__(self, task_id: int) -> None:
        self._taskset_gateway.delete_by_id(task_id)
        self._uow.commit()
