import sqlalchemy as sa
from sqlalchemy import orm

from app import entities
from app.adapters.database import models
from app.services import protocols


class AnswerDBGateway(
    protocols.AnswerSaver,
    protocols.AnswerReader,
    protocols.AnswerDeleter,
):
    model = models.AnswerDBModel

    def __init__(self, session: orm.Session):
        self._session = session

    def _to_entity(
        self,
        query_model: models.AnswerDBModel,
    ) -> entities.Answer:
        return entities.Answer(
            id=query_model.id,
            data=query_model.data,
            is_correct=query_model.is_correct,
        )

    def save(self, answer: entities.Answer):
        if answer.id is None:
            instance = self.model(
                task_id=answer.task_id,
                data=answer.data,
                is_correct=answer.is_correct,
            )
            self._session.add(instance)
        else:
            query = sa.select(self.model).where(self.model.id == answer.id)
            instance = self._session.scalars(query).one()
            instance.data = answer.data
            instance.is_correct = answer.is_correct

    def save_batch(self, answers: list[entities.Answer]):
        for answer in answers:
            self.save(answer)

    def get_answer_list_by_task_id(
        self,
        task_id: int,
    ) -> list[entities.Answer]:
        query = sa.select(self.model).where(
            self.model.task_id == task_id,
        )
        instances = self._session.scalars(query)
        return [self._to_entity(instance) for instance in instances]

    def get_answer_list(self) -> list[entities.Answer]:
        query = sa.select(self.model)
        instances = self._session.scalars(query).unique().all()
        return [self._to_entity(instance) for instance in instances]

    def get_answer_by_id(self, answer_id: int) -> entities.Answer:
        query = sa.select(self.model).where(self.model.id == answer_id)
        instance = self._session.scalars(query).one()
        return self._to_entity(instance)

    def delete_by_id(self, answer_id: int):
        query = sa.select(self.model).where(self.model.id == answer_id)
        instance = self._session.scalars(query).one()
        self._session.delete(instance)

    def delete_batch_by_task_id(self, task_id: int):
        query = sa.select(self.model).where(self.model.task_id == task_id)
        instances = self._session.scalars(query)
        for instance in instances:
            self._session.delete(instance)
