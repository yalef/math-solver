from .base import BaseModel
import sqlalchemy


class TaskDBModel(BaseModel):
    __tablename__ = "task"
    id = sqlalchemy.orm.mapped_column(
        sqlalchemy.Integer,
        primary_key=True,
        nullable=False,
    )
    level = sqlalchemy.orm.mapped_column(
        sqlalchemy.Integer,
        nullable=False,
    )
    description = sqlalchemy.orm.mapped_column(
        sqlalchemy.String(200),
        nullable=False,
    )
    taskset_id = sqlalchemy.orm.mapped_column(
        sqlalchemy.ForeignKey("taskset.id"),
    )
    taskset = sqlalchemy.orm.relationship(
        "TaskSetDBModel",
        back_populates="tasks",
    )
    answers = sqlalchemy.orm.relationship(
        "AnswerDBModel",
        back_populates="task",
    )
    themes = sqlalchemy.orm.relationship(
        "ThemeDBModel",
        secondary="task_theme_proxy",
        back_populates="tasks",
    )


class TaskThemeProxyDBModel(BaseModel):
    __tablename__ = "task_theme_proxy"
    task_id = sqlalchemy.orm.mapped_column(
        sqlalchemy.ForeignKey("task.id"),
        primary_key=True,
    )
    theme_id = sqlalchemy.orm.mapped_column(
        sqlalchemy.ForeignKey("theme.id"),
        primary_key=True,
    )
