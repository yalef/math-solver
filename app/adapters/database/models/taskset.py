import sqlalchemy as sa
from sqlalchemy import orm

from .base import BaseModel


class TaskSetDBModel(BaseModel):
    __tablename__ = "taskset"
    id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer,
        primary_key=True,
        nullable=False,
    )
    name: orm.Mapped[str] = orm.mapped_column(
        sa.String(100),
        nullable=False,
    )
    tasks: orm.Mapped[list["TaskDBModel"]] = orm.relationship(
        "TaskDBModel",
        back_populates="taskset",
        lazy="joined",
    )
