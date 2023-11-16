"""add top projects view

Revision ID: e2e7e0a3055f
Revises: 0b1ba011113c
Create Date: 2023-11-16 14:03:18.262055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2e7e0a3055f'
down_revision = '0b1ba011113c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    CREATE_VIEW_SQL = """
    CREATE OR REPLACE VIEW top_overall AS
    SELECT
        p.id,
        p.name_blog,
        r.rating_overall
    FROM
        projects p
    JOIN
        rating r ON p.id = r.project_id
    ORDER BY
        r.rating_overall DESC
    LIMIT 5
    """
    op.execute(CREATE_VIEW_SQL)

def downgrade() -> None:
    DROP_VIEW_SQL = "DROP VIEW IF EXISTS top_overall"
    op.execute(DROP_VIEW_SQL)