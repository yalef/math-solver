import typing
import app.entities


class AnswerSaver(typing.Protocol):
    def save(self, answer: app.entities.Answer):
        pass

    def save_batch(self, answers: list[app.entities.Answer]):
        pass


class AnswerReader(typing.Protocol):
    def get_answer_list_by_task_id(
        self,
        task_id: int,
    ) -> list[app.entities.Answer]:
        pass

    def get_answer_by_id(self, answer_id: int) -> app.entities.Answer:
        pass

    def get_answer_list(self) -> list[app.entities.Answer]:
        pass


class AnswerDeleter(typing.Protocol):
    def delete_by_id(self, answer_id: int):
        pass

    def delete_batch_by_task_id(self, task_id: int):
        pass
