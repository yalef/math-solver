from sqlalchemy import orm
import sqlalchemy as sa
from app.services import protocols
from app.adapters.database import models
from app import entities


class TaskDBGateway(
    protocols.TaskReader,
    protocols.TaskSaver,
    protocols.TaskDeleter,
):
    model = models.TaskDBModel
    relation_model = models.ThemeDBModel

    def __init__(self, session: orm.Session):
        self._session = session

    def _to_entity(
        self,
        query_model: models.TaskDBModel,
    ) -> entities.Task:
        answers = [
            entities.Answer(
                id=answer.id,
                data=answer.data,
                is_correct=answer.is_correct,
            )
            for answer in query_model.answers
        ]
        themes = [
            entities.Theme(id=theme.id, name=theme.name)
            for theme in query_model.themes
        ]
        return entities.Task(
            id=query_model.id,
            taskset_id=query_model.id,
            answers=answers,
            themes=themes,
            level=query_model.level,
            description=query_model.description,
            status=query_model.status,
        )

    def save(self, task: entities.Task):
        theme_ids = [theme.id for theme in task.themes]
        related_themes_query = sa.select(
            self.relation_model,
        ).where(self.relation_model.id.in_(theme_ids))
        related_theme_instances = self._session.scalars(
            related_themes_query,
        ).unique()
        if task.id is None:
            instance = self.model(
                taskset_id=task.taskset_id,
                description=task.description,
                level=task.level,
                status=task.status,
            )
            instance.themes.extend(related_theme_instances)
            self._session.add(instance)
        else:
            query = sa.select(self.model).where(self.model.id == task.id)
            instance = self._session.scalars(query).one()
            instance.level = task.level
            instance.description = task.description
            instance.status = task.status
            instance.themes.extend(related_theme_instances)

    def get_task_list(self) -> list[entities.Task]:
        query = sa.select(self.model)
        instances = self._session.scalars(query).unique()
        return [
            self._to_entity(instance) for instance in instances
        ]

    def get_tasks_list_by_taskset_id(
        self,
        taskset_id: int,
    ) -> list[entities.Task]:
        query = sa.select(self.model).where(
            self.model.taskset_id == taskset_id,
        )
        instances = self._session.scalars(query).unique()
        return [
            self._to_entity(instance) for instance in instances
        ]

    def get_task_by_id(self, task_id: int) -> entities.Task:
        query = sa.select(self.model).where(self.model.id == task_id)
        instance = self._session.scalars(query).one()
        return self._to_entity(instance)

    def get_tasks_by_ids(self, task_ids: list[int]) -> list[entities.Task]:
        query = sa.select(self.model).where(
            self.model.id.in_(task_ids),
        )
        instances = self._session.scalars(query).unique()
        return [
            self._to_entity(instance) for instance in instances
        ]

    def delete_by_id(self, task_id: int):
        query = sa.select(self.model).where(self.model.id == task_id)
        instance = self._session.scalars(query).one()
        self._session.delete(instance)
