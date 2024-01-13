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

    def _to_entity(
        self,
        query_model,
    ) -> app.entities.Task:
        answers = [
            app.entities.Answer(
                id=answer.id,
                task_id=answer.task_id,
                data=answer.data,
                is_correct=answer.is_correct,
            )
            for answer in query_model.answers
        ]
        themes = [
            app.entities.Theme(id=theme.id, name=theme.name) for theme in query_model.themes
        ]
        return app.entities.Task(
            id=query_model.id,
            taskset_id=query_model.taskset_id,
            answers=answers,
            themes=themes,
            level=query_model.level,
            description=query_model.description,
            status=query_model.status,
        )

    def __call__(self, task_dto: protocols.TaskDTO) -> app.entities.Task:
        themes = self._theme_gateway.get_theme_list_by_ids(task_dto.theme_ids)

        task = app.entities.Task(
            id=None,
            taskset_id=task_dto.taskset_id,
            answers=[],
            themes=themes,
            level=task_dto.level,
            description=task_dto.description,
        )

        saved_task = self._task_gateway.save(task)
        self._uow.commit()
        entity = self._to_entity(saved_task)
        return entity


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
