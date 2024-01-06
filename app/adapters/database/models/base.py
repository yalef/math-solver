import sqlalchemy.orm


class BaseModel(sqlalchemy.orm.DeclarativeBase):
    """Base class for ORM models."""

    __abstract__ = True
