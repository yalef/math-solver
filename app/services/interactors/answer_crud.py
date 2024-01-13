import app.entities
from app.services import protocols


class AnswerCreate:
    def __init__(
        self,
        uow: protocols.UoW,
        answer_gateway: protocols.AnswerSaver,
    ):
        self._uow = uow
        self._gateway = answer_gateway

    def _to_entity(self, query_model) -> app.entities.Answer:
        return app.entities.Answer(
            id=query_model.id,
            task_id=query_model.task_id,
            data=query_model.data,
            is_correct=query_model.is_correct,
        )

    def __call__(self, answer_dto: protocols.AnswerDTO) -> app.entities.Answer:
        answer = app.entities.Answer(
            id=None,
            task_id=answer_dto.task_id,
            data=answer_dto.data,
            is_correct=answer_dto.is_correct,
        )
        saved_instance = self._gateway.save(answer)
        self._uow.commit()
        entity = self._to_entity(saved_instance)
        return entity


class AnswerDelete:
    def __init__(
        self,
        uow: protocols.UoW,
        answer_gateway: protocols.AnswerDeleter,
    ):
        self._uow = uow
        self._gateway = answer_gateway

    def __call__(self, answer_id: int):
        self._gateway.delete_by_id(answer_id)
        self._uow.commit()


class AnswerGet:
    def __init__(
        self,
        uow: protocols.UoW,
        answer_gateway: protocols.AnswerReader,
    ):
        self._uow = uow
        self._gateway = answer_gateway

    def __call__(
        self,
        answer_id: int,
    ) -> app.entities.Answer:
        answer = self._gateway.get_answer_by_id(answer_id)
        self._uow.commit()
        return answer


class AnswerGetList:
    def __init__(
        self,
        uow: protocols.UoW,
        answer_gateway: protocols.AnswerReader,
    ):
        self._uow = uow
        self._gateway = answer_gateway

    def __call__(
        self,
    ) -> list[app.entities.Answer]:
        answers = self._gateway.get_answer_list()
        self._uow.commit()
        return answers
