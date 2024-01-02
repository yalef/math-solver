import sqlalchemy


class BaseModel(sqlalchemy.orm.DeclarativeBase):
    """Base class for ORM models."""
