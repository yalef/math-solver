import sqlalchemy as sa
from sqlalchemy import orm

from app import entities
from app.adapters.database import models
from app.services import protocols


class TaskSetDBGateway(
    protocols.TaskSetReader,
    protocols.TaskSetSaver,
    protocols.TaskSetDeleter,
):
    model = models.TaskSetDBModel

    def __init__(self, session: orm.Session):
        self._session = session

    def _to_entity(
        self,
        query_model: models.TaskSetDBModel,
    ) -> entities.TaskSet:
        tasks = []
        for task in query_model.tasks:
            answers = [
                entities.Answer(
                    id=answer.id,
                    data=answer.data,
                    is_correct=answer.is_correct,
                )
                for answer in task.answers
            ]
            themes = [
                entities.Theme(id=theme.id, name=theme.name) for theme in task.themes
            ]
            tasks.append(
                entities.Task(
                    id=task.id,
                    taskset_id=query_model.id,
                    answers=answers,
                    themes=themes,
                    level=task.level,
                    description=task.description,
                    status=task.status,
                )
            )
        return entities.TaskSet(
            id=query_model.id,
            tasks=tasks,
            name=query_model.name,
        )

    def save(self, taskset: entities.TaskSet):
        if taskset.id is None:
            instance = self.model(name=taskset.name)
            self._session.add(instance)
        else:
            query = sa.select(self.model).where(self.model.id == taskset.id)
            instance = self._session.scalars(query).unique().one()
            instance.name = taskset.name

    def get_taskset_list(self) -> list[entities.TaskSet]:
        query = sa.select(self.model)
        instances = self._session.scalars(query).unique()
        return [self._to_entity(instance) for instance in instances]

    def get_taskset_by_id(self, taskset_id: int) -> entities.TaskSet:
        query = sa.select(self.model).where(self.model.id == taskset_id)
        instance = self._session.scalars(query).unique().one()
        return self._to_entity(instance)

    def delete_by_id(self, taskset_id: int):
        query = sa.select(self.model).where(self.model.id == taskset_id)
        instance = self._session.scalars(query).unique().one()
        self._session.delete(instance)
