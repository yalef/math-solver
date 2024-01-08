import app.entities
from app.services import protocols


class TaskGet:
    def __init__(
        self,
        uow: protocols.UoW,
        task_gateway: protocols.TaskReader,
    ):
        self._uow = uow
        self._task_gateway = task_gateway

    def __call__(self, task_id: int) -> app.entities.Task:
        task = self._task_gateway.get_task_by_id(task_id)
        self._uow.commit()
        return task


class TaskGetList:
    def __init__(
        self,
        uow: protocols.UoW,
        task_gateway: protocols.TaskReader,
    ):
        self._uow = uow
        self._task_gateway = task_gateway

    def __call__(self) -> list[app.entities.Task]:
        tasks = self._task_gateway.get_task_list()
        self._uow.commit()
        return tasks


class TaskCreate:
    def __init__(
        self,
        uow: protocols.UoW,
        task_gateway: protocols.TaskSaver,
        theme_gateway: protocols.ThemeReader,
    ):
        self._uow = uow
        self._task_gateway = task_gateway
        self._theme_gateway = theme_gateway

    def __call__(self, task_dto: protocols.TaskDTO) -> None:
        themes = self._theme_gateway.get_theme_list_by_ids(task_dto.theme_ids)

        task = app.entities.Task(
            id=None,
            taskset_id=task_dto.taskset_id,
            answers=[],
            themes=themes,
            level=task_dto.level,
            description=task_dto.description,
        )

        self._task_gateway.save(task)
        self._uow.commit()
        return task


class TaskDelete:
    def __init__(
        self,
        uow: protocols.UoW,
        task_gateway: protocols.TaskDeleter,
        answer_gateway: protocols.AnswerDeleter,
    ):
        self._uow = uow
        self._task_gateway = task_gateway
        self._answer_gateway = answer_gateway

    def __call__(self, task_id: int):
        self._task_gateway.delete_by_id(task_id)
        self._answer_gateway.delete_batch_by_task_id(task_id)
        self._uow.commit()
