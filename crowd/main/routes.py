from flask import Blueprint, render_template, url_for, redirect
from crowd.main.form import HomeForm
from crowd.models import db, Project, User
from flask_login import current_user
from crowd.views import UserProjectInterests

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm()
    data = Project.query.all()
    user_id = current_user.get_id()
    #user_topics = User.query.filter_by(author_id=user_id).first().topics_user

    #UserProjectInterests.create_user_project_interests(user_id)  # Создаем представление перед использованием
    #project_topics = db.session.query(UserProjectInterests).all()
    # user = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        if form.registration.data:
            return redirect(url_for('users.register'))
        elif form.authentication.data:
            return redirect(url_for('users.login'))

    return render_template('home.html', form=form, data=data)

