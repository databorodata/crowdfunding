from flask import Blueprint, render_template, url_for, redirect
from crowd.main.form import HomeForm
from crowd.models import db, Project, User, RatingProject
from flask_login import current_user
from crowd.views import view_top_rating_overall, view_top_rating_followers, view_top_interesting, view_top_profession
from sqlalchemy import text

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()

    view_top_rating_overall()
    top_rating_project = db.session.query(Project.id, Project.name_blog).from_statement(
        text('SELECT * FROM top_overall')
    ).all()
    view_top_rating_followers()
    top_rating_followers = db.session.query(Project.id, Project.name_blog).from_statement(
        text('SELECT * FROM top_followers')
    ).all()

    top_rating_topics, top_profession_topics = [], []
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user_topics = set(User.query.filter_by(id=user_id).first().topics_user)
        view_top_interesting()

        if user_topics:
            top_interesting = db.session.query(
                Project.id.label("project_id"),
                Project.name_blog.label("name_blog"),
                Project.topic_blog.label("topic_blog"),
                RatingProject.rating_overall.label("rating_overall")
            ).from_statement(text('SELECT * FROM top_interesting')).all()
            top_rating_topics = []
            for project in top_interesting:
                if project[2][0] in user_topics:
                    top_rating_topics.append(project)

        user_profession = User.query.filter_by(id=user_id).first().profession[0]
        if user_profession:
            view_top_profession(user_profession)
            top_profession_topics = db.session.query(
                Project.id.label("project_id"),
                Project.name_blog.label("name_blog"),
                Project.topic_blog.label("topic_blog"),
                RatingProject.rating_overall.label("rating_specialists")).from_statement(
                text('SELECT * FROM view_top_profession')).all()

    if form.validate_on_submit():
        if form.registration.data:
            return redirect(url_for('users.register'))
        elif form.authentication.data:
            return redirect(url_for('users.login'))

    return render_template(
        'home.html', form=form,
        top_rating_project=top_rating_project,
        top_rating_followers=top_rating_followers,
        top_rating_topics=top_rating_topics,
        top_profession_topics=top_profession_topics
    )
