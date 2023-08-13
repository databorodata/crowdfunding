from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_user, login_required, logout_user, current_user

from crowd.models import db, User, ParticipantInfo
from crowd.user.form import RegisterForm, LoginForm, ParticipantForm
from crowd import bcrypt

users = Blueprint('users', __name__)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             if bcrypt.check_password_hash(user.password, form.password.data):
#                 login_user(user)
#                 return redirect(url_for('dashboard'))
#     return render_template('login.html', form=form)


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
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)



@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


# @app.route('/dashboard', methods=['GET', 'POST'])
# @login_required
# def dashboard():
#     form = SelectForm()
#
#     if form.validate_on_submit():
#         if form.authorinfo.data:
#             return redirect(url_for('authorform'))
#         elif form.partinfo.data:
#             return redirect(url_for('partform'))
#         elif form.newproject.data:
#             return redirect(url_for('newproject'))
#
#     return render_template('dashboard.html', form=form)



@users.route('/partform', methods=['GET', 'POST'])
@login_required
def partform():
    form = ParticipantForm()
    if form.validate_on_submit():
        user_id = current_user.get_id()
        copyrighter_, contenteditor_ = False, False
        profession = form.profession.data["prof"]
        for p in profession:
            if p == "copyrighter": copyrighter_ = True
            elif p == "contenteditor": contenteditor_ = True
        newinfo = ParticipantInfo(my_skills=form.my_skills.data, my_experience=form.my_experience.data,
                                  copyrighter=copyrighter_, contenteditor=contenteditor_, part_id=user_id)
        db.session.add(newinfo)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('partform.html', form=form)
