"""add project and join table

Revision ID: a9dca79be434
Revises: f82dd42f0e7a
Create Date: 2023-08-21 10:35:23.090952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9dca79be434'
down_revision = 'f82dd42f0e7a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name_blog', sa.String, nullable=False),
        sa.Column('name_product', sa.String, nullable=False),
        sa.Column('product_quantity', sa.Integer, nullable=False),
        sa.Column('price_author', sa.Integer, nullable=False),
        sa.Column('price_part' ,sa.Integer, nullable=False),
        sa.Column('follower', sa.Integer, nullable=True),
        sa.Column('salary_follower', sa.Integer, nullable=True),
        sa.Column('copyrighter', sa.Integer, nullable=True),
        sa.Column('salary_copyrighter' ,sa.Integer, nullable=True),
        sa.Column('contenteditor', sa.Integer, nullable=True),
        sa.Column('salary_contenteditor', sa.Integer, nullable=True),
        sa.Column('author_id', sa.Integer, nullable=False),
        sa.Column('quantity_follower', sa.Integer, default=0),
        sa.Column('quantity_copyrighter', sa.Integer, default=0),
        sa.Column('quantity_contenteditor', sa.Integer, default=0)
    )

    op.create_table(
        'joinpart`',
        sa.Column('project_id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('join_follower', sa.Boolean, default=False),
        sa.Column('join_copyrighter', sa.Boolean, default=False),
        sa.Column('join_contenteditor', sa.Boolean, default=False)
    )



def downgrade() -> None:
    op.drop_table('projects')
    op.drop_table('joinpart')
