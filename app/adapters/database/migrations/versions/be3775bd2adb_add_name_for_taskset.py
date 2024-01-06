"""add name for taskset

Revision ID: be3775bd2adb
Revises: 8d0947121951
Create Date: 2024-01-06 15:53:15.175799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be3775bd2adb'
down_revision: Union[str, None] = '8d0947121951'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('taskset', sa.Column('name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('taskset', 'name')
    # ### end Alembic commands ###
