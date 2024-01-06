"""init

Revision ID: cedbf6739872
Revises: 
Create Date: 2024-01-03 00:43:50.561355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cedbf6739872"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "taskset",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "theme",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "task",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=200), nullable=False),
        sa.Column("taskset_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["taskset_id"],
            ["taskset.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "answer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.String(length=50), nullable=False),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["task.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "task_theme_proxy",
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("theme_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["task.id"],
        ),
        sa.ForeignKeyConstraint(
            ["theme_id"],
            ["theme.id"],
        ),
        sa.PrimaryKeyConstraint("task_id", "theme_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task_theme_proxy")
    op.drop_table("answer")
    op.drop_table("task")
    op.drop_table("theme")
    op.drop_table("taskset")
    # ### end Alembic commands ###