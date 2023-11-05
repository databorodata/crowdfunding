"""view

Revision ID: 202173dd66ff
Revises: 92722ae64780
Create Date: 2023-11-04 19:01:06.732065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202173dd66ff'
down_revision = '92722ae64780'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.execute(
        sa.text(
            """
            CREATE OR REPLACE VIEW user_project_interests AS
            SELECT
                p.id as project_id,
                p.name_blog as project_name,
                unnest(p.topic_blog) as project_topic,
                unnest(u.topics_user) as user_topic
            FROM
                projects p
            JOIN
                users u ON true
            WHERE
                u.id = 1;
            """
        ).params(user_id=None)  # None - это значение по умолчанию, которое будет заменено в момент выполнения миграции
    )

def downgrade() -> None:
    op.execute("DROP VIEW IF EXISTS user_project_interests;")
