"""fix project table

Revision ID: bd7f7c604c80
Revises: c5a3d53e11fe
Create Date: 2023-11-12 15:12:06.270352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd7f7c604c80'
down_revision = 'c5a3d53e11fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name_blog', sa.String, nullable=False),
        sa.Column('idea_blog', sa.String, nullable=False),

        sa.Column('topic_blog', sa.ARRAY(sa.String), nullable=False),

        sa.Column('name_product', sa.String, nullable=False),
        sa.Column('price_author', sa.Integer, nullable=False),

        sa.Column('count_posts', sa.Integer, nullable=False),
        sa.Column('placement_sites', sa.ARRAY(sa.String), nullable=False),
        sa.Column('count_months', sa.Integer, nullable=False),

        sa.Column('copyrighter', sa.Integer, nullable=True),
        sa.Column('salary_copyrighter', sa.Integer, nullable=True),

        sa.Column('videographer', sa.Integer, nullable=True),
        sa.Column('salary_videographer', sa.Integer, nullable=True),

        sa.Column('director', sa.Integer, nullable=True),
        sa.Column('salary_director', sa.Integer, nullable=True),

        sa.Column('scriptwriter', sa.Integer, nullable=True),
        sa.Column('salary_scriptwriter', sa.Integer, nullable=True),

        sa.Column('producer', sa.Integer, nullable=True),
        sa.Column('salary_producer', sa.Integer, nullable=True),

        sa.Column('graphicdesigner', sa.Integer, nullable=True),
        sa.Column('salary_graphicdesigner', sa.Integer, nullable=True),

        sa.Column('soundengineer', sa.Integer, nullable=True),
        sa.Column('salary_soundengineer', sa.Integer, nullable=True),

        sa.Column('lightingtechnician', sa.Integer, nullable=True),
        sa.Column('salary_lightingtechnician', sa.Integer, nullable=True),

        sa.Column('seospecialist', sa.Integer, nullable=True),
        sa.Column('salary_seospecialist', sa.Integer, nullable=True),

        sa.Column('communitymanager', sa.Integer, nullable=True),
        sa.Column('salary_communitymanager', sa.Integer, nullable=True),

        sa.Column('monetizationspecialist', sa.Integer, nullable=True),
        sa.Column('salary_monetizationspecialist', sa.Integer, nullable=True),

        sa.Column('salary_all_professionals', sa.Integer, nullable=True),
        sa.Column('salary_follower', sa.Integer, nullable=True),
        sa.Column('total_salary_follower', sa.Integer, nullable=True),
        sa.Column('count_followers', sa.Integer, nullable=True),
        sa.Column('amount_project', sa.Integer, nullable=True),
        sa.Column('price_product', sa.Integer, nullable=True),
        sa.Column('count_product', sa.Integer, nullable=True),
        sa.Column('amount_donate', sa.Integer, nullable=True),
        sa.Column('amount_order_product', sa.Integer, nullable=True),

        sa.Column('author_id', sa.Integer, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('projects')
