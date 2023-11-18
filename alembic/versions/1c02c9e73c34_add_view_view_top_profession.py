"""add view view_top_profession

Revision ID: 1c02c9e73c34
Revises: 03b788e7902d
Create Date: 2023-11-18 16:51:05.008632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c02c9e73c34'
down_revision = '03b788e7902d'
branch_labels = None
depends_on = None

def upgrade() -> None:
    CREATE_VIEW_SQL = """
        CREATE OR REPLACE VIEW view_top_profession AS
        SELECT
            p.id AS project_id,
            p.name_blog,
            p.topic_blog,
            r.rating_specialists,
            p.copyrighter,
            p.videographer,
            p.director,
            p.scriptwriter,
            p.graphicdesigner,
            p.producer,
            p.soundengineer,
            p.lightingtechnician,
            p.seospecialist,
            p.communitymanager,
            p.monetizationspecialist
        FROM
            projects p
        JOIN
            rating r ON p.id = r.project_id
        WHERE
            p.director > 0
        ORDER BY
            r.rating_specialists DESC
        LIMIT 3
    """
    op.execute(CREATE_VIEW_SQL)


def downgrade() -> None:
    DROP_VIEW_SQL = "DROP VIEW IF EXISTS view_top_profession"
    op.execute(DROP_VIEW_SQL)