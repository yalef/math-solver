import sqlalchemy as sa
from sqlalchemy import orm


def build_engine(db_url: str) -> sa.Engine:
    engine = sa.create_engine(
        url=db_url,
        echo=True,
    )
    return engine


def build_session_factory(engine: sa.Engine) -> orm.sessionmaker:
    session_factory = orm.sessionmaker(bind=engine)
    return session_factory
