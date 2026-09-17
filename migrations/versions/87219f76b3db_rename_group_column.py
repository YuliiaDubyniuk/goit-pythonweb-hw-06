"""rename group column

Revision ID: 87219f76b3db
Revises: dd781285c6a2
Create Date: 2026-09-17 10:33:15.473113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87219f76b3db'
down_revision: Union[str, Sequence[str], None] = 'dd781285c6a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'groups',
        'full_name',
        new_column_name='name',
        existing_type=sa.String(length=50),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        'groups',
        'name',
        new_column_name='full_name',
        existing_type=sa.String(length=50),
        existing_nullable=False,
    )
