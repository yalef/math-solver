import sqlalchemy
from .base import BaseModel


class TaskSetDBModel(BaseModel):
    __tablename__ = "taskset"
    id = sqlalchemy.orm.mapped_column(
        sqlalchemy.Integer,
        primary_key=True,
        nullable=False,
    )
    tasks = sqlalchemy.orm.relationship(
        "TaskDBModel",
        back_populates="taskset",
    )
