from app.services import protocols
import sqlalchemy


class DBUoW(protocols.UoW):
    def __init__(
        self,
        session: sqlalchemy.orm.Session,
    ):
        self._session = session

    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        self.rollback()
        self._session.close()

    def rollback(self):
        self._session.rollback()

    def commit(self):
        self._session.commit()
