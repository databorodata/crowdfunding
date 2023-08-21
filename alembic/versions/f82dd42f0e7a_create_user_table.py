"""create user table

Revision ID: f82dd42f0e7a
Revises: 
Create Date: 2023-08-20 10:50:53.017111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f82dd42f0e7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(20), nullable=False, unique=True),
        sa.Column('password', sa.String(80), nullable=False),
        sa.Column('my_skills', sa.String(1000), nullable=False),
        sa.Column('my_experience', sa.String(1000), nullable=False),
        sa.Column('copyrighter', sa.Boolean, nullable=False),
        sa.Column('contenteditor', sa.Boolean, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')