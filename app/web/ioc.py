import typing
from app.services import interactors


class InteractorFactory(typing.Protocol):
    def get_theme_by_id(
        self,
    ) -> typing.ContextManager[interactors.ThemeGet]:
        pass

    def get_theme_list(
        self,
    ) -> typing.ContextManager[interactors.ThemeCreate]:
        pass

    def delete_theme_by_id(
        self,
    ) -> typing.ContextManager[interactors.ThemeDelete]:
        pass

    def create_theme(
        self,
    ) -> typing.ContextManager[interactors.ThemeCreate]:
        pass

    def get_answer_by_id(
        self,
    ) -> typing.ContextManager[interactors.AnswerGet]:
        pass

    def get_answer_list(
        self,
    ) -> typing.ContextManager[interactors.AnswerGetList]:
        pass

    def delete_answer_by_id(
        self,
    ) -> typing.ContextManager[interactors.AnswerDelete]:
        pass

    def create_answer(
        self,
    ) -> typing.ContextManager[interactors.AnswerCreate]:
        pass

    def get_task_by_id(
        self,
    ) -> typing.ContextManager[interactors.TaskGet]:
        pass

    def get_task_list(
        self,
    ) -> typing.ContextManager[interactors.TaskGetList]:
        pass

    def delete_task_by_id(
        self,
    ) -> typing.ContextManager[interactors.TaskDelete]:
        pass

    def create_task(
        self,
    ) -> typing.ContextManager[interactors.TaskCreate]:
        pass
