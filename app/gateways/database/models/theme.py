import sqlalchemy
from .base import BaseModel


class ThemeDBModel(BaseModel):
    __tablename__ = "theme"
    id = sqlalchemy.orm.mapped_column(
        sqlalchemy.Integer,
        primary_key=True,
        nullable=False,
    )
    name = sqlalchemy.orm.mapped_column(
        sqlalchemy.String(50),
        nullable=False,
    )
    tasks = sqlalchemy.orm.relationship(
        "TaskDBModel",
        secondary="task_theme_proxy",
        back_populates="themes",
    )
