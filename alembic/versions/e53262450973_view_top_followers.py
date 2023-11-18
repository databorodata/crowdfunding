"""view top followers

Revision ID: e53262450973
Revises: e2e7e0a3055f
Create Date: 2023-11-16 18:44:18.323212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e53262450973'
down_revision = 'e2e7e0a3055f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    CREATE_VIEW_SQL = """
    CREATE OR REPLACE VIEW top_followers AS
    SELECT
        p.id,
        p.name_blog,
        r.rating_followers
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
    DROP_VIEW_SQL = "DROP VIEW IF EXISTS top_followers"
    op.execute(DROP_VIEW_SQL)
