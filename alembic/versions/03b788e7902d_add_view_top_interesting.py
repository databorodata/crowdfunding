"""add view top_interesting

Revision ID: 03b788e7902d
Revises: e53262450973
Create Date: 2023-11-18 14:08:34.653816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b788e7902d'
down_revision = 'e53262450973'
branch_labels = None
depends_on = None


def upgrade() -> None:
    CREATE_VIEW_SQL = """
        CREATE OR REPLACE VIEW top_interesting AS
        SELECT
          p.id AS project_id,
          p.name_blog AS name_blog,
          p.topic_blog AS topic_blog,
          r.rating_overall AS rating_overall
        FROM
          projects p
        JOIN
          rating r ON p.id = r.project_id
        WHERE
          (p.topic_blog, r.rating_overall) IN (
            SELECT
              p2.topic_blog,
              r2.rating_overall
            FROM
              projects p2
            JOIN
              rating r2 ON p2.id = r2.project_id
            WHERE
              p2.topic_blog = p.topic_blog
            ORDER BY
              r2.rating_overall DESC
            LIMIT 3
          )
        ORDER BY
          p.topic_blog, r.rating_overall DESC;
    """
    op.execute(CREATE_VIEW_SQL)


def downgrade() -> None:
    DROP_VIEW_SQL = "DROP VIEW IF EXISTS top_interesting"
    op.execute(DROP_VIEW_SQL)
