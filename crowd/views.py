from sqlalchemy import text
from crowd.models import db

def view_top_rating_overall():
    CREATE_VIEW_SQL = text("""
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
    """)
    db.session.execute(CREATE_VIEW_SQL)
    db.session.commit()

def view_top_rating_followers():
    CREATE_VIEW_SQL = text("""
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
    """)
    db.session.execute(CREATE_VIEW_SQL)
    db.session.commit()


def view_top_interesting():
    CREATE_VIEW_SQL = text('''
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
        ''')
    db.session.execute(CREATE_VIEW_SQL)
    db.session.commit()




# def view_top_followers_project():
#     CREATE_VIEW_SQL = text("""
#     CREATE OR REPLACE VIEW top_projects AS
#     SELECT
#         p.id as project_id,
#         p.name_blog as project_name,
#         r.rating_followers as project_rating
#     FROM
#         projects p
#     JOIN
#         rating r ON p.id = r.project_id
#     ORDER BY
#         r.rating_followers DESC
#     LIMIT 5
#     """)
#
#     # Отключаем автоматическое фиксирование транзакций
#     with db.session.begin(subtransactions=True):
#         db.session.execute(CREATE_VIEW_SQL)
#
#     # Используем TextClause для явного указания столбца 'project_id'
#     projects = db.session.query(text('project_id')).from_statement(text('SELECT * FROM top_projects')).all()
#     project_ids = [project[0] for project in projects]
#     return project_ids
#



# class UserProjectInterests(db.Model):
#     __tablename__ = 'user_project_interests'
#
#     project_id = db.Column(db.Integer, primary_key=True)
#     project_name = db.Column(db.String)
#     topic_blog = db.Column(db.ARRAY(db.String()))
#
#     @staticmethod
#     def create_user_project_interests(user_id):
#         CREATE_VIEW_SQL = text("""
#         CREATE OR REPLACE VIEW user_project_interests AS
#         SELECT
#             p.id as project_id,
#             p.name_blog as project_name,
#             unnest(p.topic_blog) as project_topic,
#             unnest(u.topics_user) as user_topic
#         FROM
#             projects p
#         JOIN
#             users u ON true
#         WHERE
#             u.id = :user_id
#         """)
#         db.session.execute(CREATE_VIEW_SQL, {'user_id': user_id})
#         db.session.commit()




