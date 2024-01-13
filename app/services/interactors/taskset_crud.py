import app.entities
from app.services import protocols


class TaskSetGet:
    def __init__(
        self,
        uow: protocols.UoW,
        taskset_gateway: protocols.TaskSetReader,
    ):
        self._uow = uow
        self._taskset_gateway = taskset_gateway

    def __call__(self, taskset_id: int) -> app.entities.TaskSet:
        taskset = self._taskset_gateway.get_taskset_by_id(taskset_id)
        self._uow.commit()
        return taskset


class TaskSetGetList:
    def __init__(
        self,
        uow: protocols.UoW,
        taskset_gateway: protocols.TaskSetReader,
    ):
        self._uow = uow
        self._taskset_gateway = taskset_gateway

    def __call__(self) -> app.entities.TaskSet:
        taskset = self._taskset_gateway.get_taskset_list()
        self._uow.commit()
        return taskset


class TaskSetCreate:
    def __init__(
        self,
        uow: protocols.UoW,
        taskset_gateway: protocols.TaskSetSaver,
    ):
        self._uow = uow
        self._taskset_gateway = taskset_gateway

    def __call__(self, taskset_dto: protocols.TaskSetDTO) -> app.entities.TaskSet:
        taskset = app.entities.TaskSet(
            id=None,
            name=taskset_dto.name,
            tasks=[],
        )
        saved_taskset = self._taskset_gateway.save(taskset)
        self._uow.commit()
        return saved_taskset


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
