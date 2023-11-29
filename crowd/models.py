from flask_login import UserMixin
from crowd import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Project(db.Model):
    __tablename__ = 'projects'

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

    author_id = db.Column(db.Integer, nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    my_skills = db.Column(db.String(1000), nullable=True)
    my_experience = db.Column(db.String(1000), nullable=True)
    profession = db.Column(db.ARRAY(db.String()), nullable=True)
    # Добавляем GIN индекс для колонки profession
    # professions_index = db.Index('professions_index', profession, postgresql_using='gin')
    topics_user = db.Column(db.ARRAY(db.String()), nullable=True)
    participation_projects = db.Column(db.ARRAY(db.Integer()), nullable=True, default=[])


class RatingProject(db.Model):
    __tablename__ = 'rating'
    project_id = db.Column(db.Integer, nullable=False, primary_key=True)
    rating_followers = db.Column(db.Float, default=0.0, nullable=True)
    rating_promotion = db.Column(db.Float, default=0.0, nullable=True)
    rating_specialists = db.Column(db.Float, default=0.0, nullable=True)
    rating_overall = db.Column(db.Float, default=0.0, nullable=True)


class JoinProject(db.Model):
    __tablename__ = 'joinpart'
    project_id = db.Column(db.Integer, nullable=False, primary_key=True)
    join_follower = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_copyrighter = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_videographer = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_director = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_scriptwriter = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_graphicdesigner = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_producer = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_soundengineer = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_lightingtechnician = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_seospecialist = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_communitymanager = db.Column(db.ARRAY(db.Integer()), nullable=False)
    join_monetizationspecialist = db.Column(db.ARRAY(db.Integer()), nullable=False)

