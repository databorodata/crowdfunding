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


def view_top_profession(profession):
    CREATE_VIEW_SQL = text(f'''
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
            p.{profession} > 0
        ORDER BY
            r.rating_specialists DESC
        LIMIT 3
    ''')

    db.session.execute(CREATE_VIEW_SQL)
    db.session.commit()
