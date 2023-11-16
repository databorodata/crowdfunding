"""add view top_followers

Revision ID: 0b1ba011113c
Revises: bd7f7c604c80
Create Date: 2023-11-16 12:37:54.131446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b1ba011113c'
down_revision = 'bd7f7c604c80'
branch_labels = None
depends_on = None


def upgrade() -> None:
    CREATE_VIEW_SQL = """
    CREATE OR REPLACE VIEW top_projects AS
    SELECT
        p.id as project_id,
        p.name_blog as project_name,
        r.rating_followers as project_rating
    FROM
        projects p
    JOIN
        rating r ON p.id = r.project_id
    ORDER BY
        r.rating_followers DESC
    LIMIT 5
    """
    op.execute(CREATE_VIEW_SQL)

def downgrade() -> None:
    DROP_VIEW_SQL = "DROP VIEW IF EXISTS top_projects"
    op.execute(DROP_VIEW_SQL)