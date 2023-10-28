"""fix users table

Revision ID: 92722ae64780
Revises: a9dca79be434
Create Date: 2023-08-25 10:25:49.943504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92722ae64780'
down_revision = 'a9dca79be434'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(20), nullable=False, unique=True),
        sa.Column('password', sa.String(80), nullable=False),
        sa.Column('my_skills', sa.String(1000), nullable=True),
        sa.Column('my_experience', sa.String(1000), nullable=True),
        sa.Column('copyrighter', sa.Boolean, nullable=True),
        sa.Column('contenteditor', sa.Boolean, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('users')