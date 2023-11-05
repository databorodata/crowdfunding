from sqlalchemy import text
from crowd.models import db
class UserProjectInterests(db.Model):
    __tablename__ = 'user_project_interests'

    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String)
    topic_blog = db.Column(db.ARRAY(db.String()))

    @staticmethod
    def create_user_project_interests(user_id):
        CREATE_VIEW_SQL = text("""
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
            u.id = :user_id
        """)
        db.session.execute(CREATE_VIEW_SQL, {'user_id': user_id})
        db.session.commit()