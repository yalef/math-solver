import sqlalchemy
from .base import BaseModel


class AnswerDBModel(BaseModel):
    __tablename__ = "answer"
    id = sqlalchemy.orm.mapped_column(
        sqlalchemy.Integer,
        primary_key=True,
        nullable=False,
    )
    data = sqlalchemy.orm.mapped_column(
        sqlalchemy.String(50),
        nullable=False,
    )
    is_correct = sqlalchemy.orm.mapped_column(
        sqlalchemy.Boolean,
        nullable=False,
        default=True,
    )
    task_id = sqlalchemy.orm.mapped_column(sqlalchemy.ForeignKey("task.id"))
    task = sqlalchemy.orm.relationship(
        "TaskDBModel",
        back_populates="answers",
    )
