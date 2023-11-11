from flask import render_template, url_for, redirect, Blueprint, request
from flask_login import login_user, login_required, logout_user, current_user

from crowd.models import db, User, Project
from crowd.user.form import RegisterForm, LoginForm, ParticipantForm, SelectForm
from crowd import bcrypt

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.home'))
    return render_template('login.html', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password, profession = [''],
                        my_skills='', my_experience='', topics_user=[''])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)



@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    user_id = current_user.get_id()

    form = SelectForm()
    part = User.query.filter_by(id=user_id).first()
    project = Project.query.filter_by(author_id=user_id).first()

    if form.validate_on_submit():
        if form.partinfo.data:
            return redirect(url_for('users.partform'))
        elif form.editproject.data:
            return redirect(url_for('projects.edit_project'))
        elif form.newproject.data:
            return redirect(url_for('projects.create_project'))

    return render_template('dashboard.html', part=part, project=project, form=form)

@users.route('/partform', methods=['GET', 'POST'])
@login_required
def partform():
    form = ParticipantForm()
    user_id = current_user.get_id()
    user_info = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        user_info.my_skills = form.my_skills.data
        user_info.my_experience = form.my_experience.data
        user_info.profession = form.profession.data
        user_info.topics_user = form.topics_user.data
        form.populate_obj(user_info)
        db.session.commit()
        return redirect(url_for('users.dashboard'))

    return render_template('partform.html', form=form)



