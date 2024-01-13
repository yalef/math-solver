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

    def _to_entity(
        self,
        query_model,
    ) -> app.entities.TaskSet:
        tasks = []
        for task in query_model.tasks:
            answers = [
                app.entities.Answer(
                    id=answer.id,
                    data=answer.data,
                    is_correct=answer.is_correct,
                )
                for answer in task.answers
            ]
            themes = [
                app.entities.Theme(id=theme.id, name=theme.name)
                for theme in task.themes
            ]
            tasks.append(
                app.entities.Task(
                    id=task.id,
                    taskset_id=query_model.id,
                    answers=answers,
                    themes=themes,
                    level=task.level,
                    description=task.description,
                    status=task.status,
                )
            )
        return app.entities.TaskSet(
            id=query_model.id,
            tasks=tasks,
            name=query_model.name,
        )

    def __call__(self, taskset_dto: protocols.TaskSetDTO) -> app.entities.TaskSet:
        taskset = app.entities.TaskSet(
            id=None,
            name=taskset_dto.name,
            tasks=[],
        )
        saved_taskset = self._taskset_gateway.save(taskset)
        self._uow.commit()
        entity = self._to_entity(saved_taskset)
        return entity


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
