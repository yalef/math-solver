import sqlalchemy as sa
from sqlalchemy import orm
from .base import BaseModel


class AnswerDBModel(BaseModel):
    __tablename__ = "answer"
    id: orm.Mapped[int] = orm.mapped_column(
        sa.Integer,
        primary_key=True,
        nullable=False,
    )
    data: orm.Mapped[str] = orm.mapped_column(
        sa.String(50),
        nullable=False,
    )
    is_correct: orm.Mapped[bool] = orm.mapped_column(
        sa.Boolean,
        nullable=False,
        default=True,
    )
    task_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("task.id"))
    task: orm.Mapped["TaskDBModel"] = orm.relationship(
        "TaskDBModel",
        back_populates="answers",
        lazy="joined",
    )
