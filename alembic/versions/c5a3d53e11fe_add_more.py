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
    )
    id = db.Column(db.Integer, primary_key=True)
    name_blog = db.Column(db.String, nullable=False)
    idea_blog = db.Column(db.String, nullable=False)

    topic_blog = db.Column(db.ARRAY(db.String()), nullable=False)

    name_product = db.Column(db.String, nullable=False)
    price_author = db.Column(db.Integer, nullable=False)

    count_posts = db.Column(db.Integer, nullable=False)
    placement_sites = db.Column(db.ARRAY(db.String()), nullable=False)
    count_months = db.Column(db.Integer, nullable=False)

    copyrighter = db.Column(db.Integer, default=0, nullable=True)
    salary_copyrighter = db.Column(db.Integer, default=0, nullable=True)
    videographer = db.Column(db.Integer, default=0, nullable=True)
    salary_videographer = db.Column(db.Integer, default=0, nullable=True)
    director = db.Column(db.Integer, default=0, nullable=True)
    salary_director = db.Column(db.Integer, default=0, nullable=True)
    scriptwriter = db.Column(db.Integer, default=0, nullable=True)
    salary_scriptwriter = db.Column(db.Integer, default=0, nullable=True)
    graphicdesigner = db.Column(db.Integer, default=0, nullable=True)
    salary_graphicdesigner = db.Column(db.Integer, default=0, nullable=True)
    producer = db.Column(db.Integer, default=0, nullable=True)
    salary_producer = db.Column(db.Integer, default=0, nullable=True)
    soundengineer = db.Column(db.Integer, default=0, nullable=True)
    salary_soundengineer = db.Column(db.Integer, default=0, nullable=True)
    lightingtechnician = db.Column(db.Integer, default=0, nullable=True)
    salary_lightingtechnician = db.Column(db.Integer, default=0, nullable=True)
    seospecialist = db.Column(db.Integer, default=0, nullable=True)
    salary_seospecialist = db.Column(db.Integer, default=0, nullable=True)
    communitymanager = db.Column(db.Integer, default=0, nullable=True)
    salary_communitymanager = db.Column(db.Integer, default=0, nullable=True)
    monetizationspecialist = db.Column(db.Integer, default=0, nullable=True)
    salary_monetizationspecialist = db.Column(db.Integer, default=0, nullable=True)

    salary_all_professionals = db.Column(db.Integer, default=0, nullable=True)
    salary_follower = db.Column(db.Integer, default=0, nullable=True)
    total_salary_follower = db.Column(db.Integer, default=0, nullable=True)
    count_followers = db.Column(db.Integer, default=100, nullable=True)
    amount_project = db.Column(db.Integer, default=0, nullable=True)
    price_product = db.Column(db.Integer, default=0, nullable=True)
    count_product = db.Column(db.Integer, default=0, nullable=True)
    amount_donate = db.Column(db.Integer, default=0, nullable=True)
    amount_order_product = db.Column(db.Integer, default=0, nullable=True)

def downgrade() -> None:
    pass
