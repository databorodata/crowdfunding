"""add more

Revision ID: c5a3d53e11fe
Revises: 202173dd66ff
Create Date: 2023-11-11 15:02:27.133348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5a3d53e11fe'
down_revision = '202173dd66ff'
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

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(20), nullable=False, unique=True),
        sa.Column('password', sa.String(80), nullable=False),
        sa.Column('my_skills', sa.String(1000), nullable=False),
        sa.Column('my_experience', sa.String(1000), nullable=False),
        sa.Column('profession', sa.ARRAY(sa.String), nullable=True),
        sa.Column('topics_user', sa.ARRAY(sa.String), nullable=True),
        sa.Column('participation_projects', sa.ARRAY(sa.String), nullable=True),
    )

    op.create_table(
        'joinpart',
        sa.Column('project_id', sa.Integer, primary_key=True),
        sa.Column('join_follower', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_copyrighter', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_videographer', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_director', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_scriptwriter', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_graphicdesigner', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_producer', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_soundengineer', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_lightingtechnician', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_seospecialist', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_communitymanager', sa.ARRAY(sa.Integer), nullable=False),
        sa.Column('join_monetizationspecialist', sa.ARRAY(sa.Integer), nullable=False)
    )

    op.create_table(
        'rating',
        sa.Column('project_id', sa.Integer, primary_key=True),
        sa.Column('rating_followers', sa.Float, nullable=True),
        sa.Column('rating_promotion', sa.Float, nullable=True),
        sa.Column('rating_specialists', sa.Float, nullable=True),
        sa.Column('rating_overall', sa.Float, nullable=True),
    )


def downgrade() -> None:
    op.drop_table('projects')
    op.drop_table('users')
    op.drop_table('joinpart')
    op.drop_table('rating')
