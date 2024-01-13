import abc
import typing

from app.services import interactors


class InteractorFactory(abc.ABC):
    @abc.abstractmethod
    def get_theme_by_id(
        self,
    ) -> typing.ContextManager[interactors.ThemeGet]:
        pass

    @abc.abstractmethod
    def get_theme_list(
        self,
    ) -> typing.ContextManager[interactors.ThemeCreate]:
        pass

    @abc.abstractmethod
    def delete_theme_by_id(
        self,
    ) -> typing.ContextManager[interactors.ThemeDelete]:
        pass

    @abc.abstractmethod
    def create_theme(
        self,
    ) -> typing.ContextManager[interactors.ThemeCreate]:
        pass

    @abc.abstractmethod
    def get_answer_by_id(
        self,
    ) -> typing.ContextManager[interactors.AnswerGet]:
        pass

    @abc.abstractmethod
    def get_answer_list(
        self,
    ) -> typing.ContextManager[interactors.AnswerGetList]:
        pass

    @abc.abstractmethod
    def delete_answer_by_id(
        self,
    ) -> typing.ContextManager[interactors.AnswerDelete]:
        pass

    @abc.abstractmethod
    def create_answer(
        self,
    ) -> typing.ContextManager[interactors.AnswerCreate]:
        pass

    @abc.abstractmethod
    def get_task_by_id(
        self,
    ) -> typing.ContextManager[interactors.TaskGet]:
        pass

    @abc.abstractmethod
    def get_task_list(
        self,
    ) -> typing.ContextManager[interactors.TaskGetList]:
        pass

    @abc.abstractmethod
    def delete_task_by_id(
        self,
    ) -> typing.ContextManager[interactors.TaskDelete]:
        pass

    @abc.abstractmethod
    def create_task(
        self,
    ) -> typing.ContextManager[interactors.TaskCreate]:
        pass

    @abc.abstractmethod
    def update_task(
        self,
    ) -> typing.ContextManager[interactors.TaskUpdate]:
        pass

    @abc.abstractmethod
    def get_taskset_by_id(
        self,
    ) -> typing.ContextManager[interactors.TaskSetGet]:
        pass

    @abc.abstractmethod
    def get_taskset_list(
        self,
    ) -> typing.ContextManager[interactors.TaskSetGetList]:
        pass

    @abc.abstractmethod
    def delete_taskset_by_id(
        self,
    ) -> typing.ContextManager[interactors.TaskSetDelete]:
        pass

    @abc.abstractmethod
    def create_taskset(
        self,
    ) -> typing.ContextManager[interactors.TaskSetCreate]:
        pass

    @abc.abstractmethod
    def solve_task(
        self,
    ) -> typing.ContextManager[interactors.TaskSetSolver]:
        pass
