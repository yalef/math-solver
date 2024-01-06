import contextlib
from app.web import ioc
from app.adapters.database import gateways
from app.adapters.database import uow
from app.adapters.database import utils
from app.services import interactors


class IoC(ioc.InteractorFactory):
    def __init__(self, db_url: str):
        self._engine = utils.build_engine(db_url)
        self._session_factory = utils.build_session_factory(self._engine)
        self._uow = uow.DBUoW
        self._theme_gateway = gateways.ThemeDBGateway
        self._task_gateway = gateways.TaskDBGateway
        self._answer_gateway = gateways.AnswerDBGateway

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
        with uow:
            yield interactors.TaskDelete(
                uow=uow,
                task_gateway=task_gateway,
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
