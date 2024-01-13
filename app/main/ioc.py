import contextlib

from app.adapters.database import gateways, uow, utils
from app.services import interactors
from app.web import ioc


class IoC(ioc.InteractorFactory):
    def __init__(self, db_url: str):
        self._engine = utils.build_engine(db_url)
        self._session_factory = utils.build_session_factory(self._engine)
        self._uow = uow.DBUoW
        self._theme_gateway = gateways.ThemeDBGateway
        self._task_gateway = gateways.TaskDBGateway
        self._answer_gateway = gateways.AnswerDBGateway
        self._taskset_gateway = gateways.TaskSetDBGateway

    @contextlib.contextmanager
    def get_theme_by_id(
        self,
    ) -> interactors.ThemeGet:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        theme_gateway = self._theme_gateway(db_session)
        with uow:
            yield interactors.ThemeGet(
                uow=uow,
                theme_gateway=theme_gateway,
            )

    @contextlib.contextmanager
    def get_theme_list(
        self,
    ) -> interactors.ThemeGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        theme_gateway = self._theme_gateway(db_session)
        with uow:
            yield interactors.ThemeGetList(
                uow=uow,
                theme_gateway=theme_gateway,
            )

    @contextlib.contextmanager
    def delete_theme_by_id(
        self,
    ) -> interactors.ThemeDelete:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        theme_gateway = self._theme_gateway(db_session)
        with uow:
            yield interactors.ThemeDelete(
                uow=uow,
                theme_gateway=theme_gateway,
            )

    @contextlib.contextmanager
    def create_theme(
        self,
    ) -> interactors.ThemeCreate:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        theme_gateway = self._theme_gateway(db_session)
        with uow:
            yield interactors.ThemeCreate(
                uow=uow,
                theme_gateway=theme_gateway,
            )

    @contextlib.contextmanager
    def get_task_by_id(
        self,
    ) -> interactors.TaskGet:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        task_gateway = self._task_gateway(db_session)
        with uow:
            yield interactors.TaskGet(
                uow=uow,
                task_gateway=task_gateway,
            )

    @contextlib.contextmanager
    def get_task_list(
        self,
    ) -> interactors.TaskGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        task_gateway = self._task_gateway(db_session)
        with uow:
            yield interactors.TaskGetList(
                uow=uow,
                task_gateway=task_gateway,
            )

    @contextlib.contextmanager
    def delete_task_by_id(
        self,
    ) -> interactors.TaskDelete:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        task_gateway = self._task_gateway(db_session)
        answer_gateway = self._answer_gateway(db_session)
        with uow:
            yield interactors.TaskDelete(
                uow=uow,
                task_gateway=task_gateway,
                answer_gateway=answer_gateway,
            )

    @contextlib.contextmanager
    def create_task(
        self,
    ) -> interactors.TaskCreate:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        task_gateway = self._task_gateway(db_session)
        theme_gateway = self._theme_gateway(db_session)
        with uow:
            yield interactors.TaskCreate(
                uow=uow,
                task_gateway=task_gateway,
                theme_gateway=theme_gateway,
            )

    @contextlib.contextmanager
    def update_task(
        self,
    ) -> interactors.TaskUpdate:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        task_gateway = self._task_gateway(db_session)
        theme_gateway = self._theme_gateway(db_session)
        with uow:
            yield interactors.TaskUpdate(
                uow=uow,
                task_gateway=task_gateway,
                theme_gateway=theme_gateway,
            )

    @contextlib.contextmanager
    def get_answer_by_id(
        self,
    ) -> interactors.AnswerGet:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        answer_gateway = self._answer_gateway(db_session)
        with uow:
            yield interactors.AnswerGet(
                uow=uow,
                answer_gateway=answer_gateway,
            )

    @contextlib.contextmanager
    def get_answer_list(
        self,
    ) -> interactors.AnswerGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        answer_gateway = self._answer_gateway(db_session)
        with uow:
            yield interactors.AnswerGetList(
                uow=uow,
                answer_gateway=answer_gateway,
            )

    @contextlib.contextmanager
    def delete_answer_by_id(
        self,
    ) -> interactors.AnswerDelete:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        answer_gateway = self._answer_gateway(db_session)
        with uow:
            yield interactors.AnswerDelete(
                uow=uow,
                answer_gateway=answer_gateway,
            )

    @contextlib.contextmanager
    def create_answer(
        self,
    ) -> interactors.AnswerCreate:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        answer_gateway = self._answer_gateway(db_session)
        with uow:
            yield interactors.AnswerCreate(
                uow=uow,
                answer_gateway=answer_gateway,
            )

    @contextlib.contextmanager
    def get_taskset_list(self) -> interactors.TaskSetGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        taskset_gateway = self._taskset_gateway(db_session)
        with uow:
            yield interactors.TaskSetGetList(
                uow=uow,
                taskset_gateway=taskset_gateway,
            )

    @contextlib.contextmanager
    def get_taskset_by_id(self) -> interactors.TaskSetGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        taskset_gateway = self._taskset_gateway(db_session)
        with uow:
            yield interactors.TaskSetGet(
                uow=uow,
                taskset_gateway=taskset_gateway,
            )

    @contextlib.contextmanager
    def delete_taskset_by_id(self) -> interactors.TaskSetGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        taskset_gateway = self._taskset_gateway(db_session)
        with uow:
            yield interactors.TaskSetDelete(
                uow=uow,
                taskset_gateway=taskset_gateway,
            )

    @contextlib.contextmanager
    def create_taskset(self) -> interactors.TaskSetGetList:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        taskset_gateway = self._taskset_gateway(db_session)
        with uow:
            yield interactors.TaskSetCreate(
                uow=uow,
                taskset_gateway=taskset_gateway,
            )

    @contextlib.contextmanager
    def solve_task(self) -> interactors.TaskSetSolver:
        db_session = self._session_factory()
        uow = self._uow(db_session)
        taskset_gateway = self._taskset_gateway(db_session)
        task_gateway = self._task_gateway(db_session)
        answer_gateway = self._answer_gateway(db_session)
        with uow:
            yield interactors.TaskSetSolver(
                uow=uow,
                task_gateway=task_gateway,
                taskset_gateway=taskset_gateway,
                answer_gateway=answer_gateway,
            )
