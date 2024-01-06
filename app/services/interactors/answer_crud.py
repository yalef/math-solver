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

    def __call__(self, answer_dto: protocols.AnswerDTO):
        answer = app.entities.Answer(
            id=answer_dto.id,
            task_id=answer_dto.task_id,
            data=answer_dto.data,
            is_correct=answer_dto.is_correct,
        )
        self._gateway.save(answer)
        self._uow.commit()


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
