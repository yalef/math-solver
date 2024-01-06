import sqlalchemy as sa
from sqlalchemy import orm

from app.entities import TaskStatus

from .base import BaseModel


class TaskDBModel(BaseModel):
    __tablename__ = "task"
    id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer,
        primary_key=True,
        nullable=False,
    )
    level: orm.Mapped[int] = orm.mapped_column(
        sa.Integer,
        nullable=False,
    )
    description: orm.Mapped[str] = orm.mapped_column(
        sa.String(200),
        nullable=False,
    )
    status: orm.Mapped[
        str
    ] = orm.mapped_column(  # use only values from `entities.TaskStatus`
        sa.String(15),
        default=TaskStatus.started,
        nullable=False,
    )
    taskset_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("taskset.id"),
    )
    taskset: orm.Mapped["TaskSetDBModel"] = orm.relationship(
        "TaskSetDBModel",
        back_populates="tasks",
        lazy="joined",
    )
    answers: orm.Mapped[list["AnswerDBModel"]] = orm.relationship(
        "AnswerDBModel",
        back_populates="task",
        lazy="joined",
    )
    themes: orm.Mapped[list["ThemeDBModel"]] = orm.relationship(
        "ThemeDBModel",
        secondary="task_theme_proxy",
        back_populates="tasks",
        lazy="joined",
    )


class TaskThemeProxyDBModel(BaseModel):
    __tablename__ = "task_theme_proxy"
    task_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("task.id"),
        primary_key=True,
    )
    theme_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("theme.id"),
        primary_key=True,
    )
