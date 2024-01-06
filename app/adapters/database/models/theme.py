import sqlalchemy as sa
from sqlalchemy import orm
from .base import BaseModel


class ThemeDBModel(BaseModel):
    __tablename__ = "theme"
    id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer,
        primary_key=True,
    )
    name: orm.Mapped[str] = orm.mapped_column(
        sa.String(50),
        nullable=False,
    )
    tasks: orm.Mapped[list["TaskDBModel"]] = orm.relationship(
        "TaskDBModel",
        secondary="task_theme_proxy",
        back_populates="themes",
        lazy="joined",
    )
