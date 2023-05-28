from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

from models import db, Project, User, AuthorInfo, ParticipantInfo
from form import HomeForm, RegisterForm, LoginForm, AuthorForm, ParticipantForm, SelectForm, NewProject

import os


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    form = HomeForm()

    if form.validate_on_submit():
        if form.registration.data:
            return redirect(url_for('register'))
        elif form.authentication.data:
            return redirect(url_for('login'))

    return render_template('home.html', form=form)


# @app.route("/projects", methods=["POST"])
# @login_required
# def create_project():
#     data = request.get_json()
#     try:
#         user_id = current_user.get_id()
#         project = Project(name=data["name"], author=user_id)
#         db.session.add(project)
#         db.session.commit()
#         return jsonify(project.serialize())
#     except Exception as e:
#         return str(e)


@app.route("/newproject", methods=["GET", "POST"])
@login_required
def create_project():
    form = NewProject()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        follower = form.team_project.follower.data
        salary_follower = form.team_project.salary_follower.data
        copyrighter = form.team_project.copyrighter.data
        salary_copyrighter = form.team_project.salary_copyrighter.data
        contenteditor = form.team_project.contenteditor.data
        salary_contenteditor = form.team_project.salary_contenteditor.data

        # if (follower and not salary_follower) or \
        #     (copyrighter and not salary_copyrighter) or \
        #     (contenteditor and not contenteditor_salary):
        #     return None
        #
        # if (salary_follower and not follower) or \
        #     (salary_copyrighter and not copyrighter) or \
        #     (salary_contenteditor and not contenteditor):
        #     return None

        project = Project(
            name_blog=form.name_blog.data,
            name_product=form.support_product.name_product.data,
            product_quantity=form.support_product.product_quantity.data,
            price_author=form.support_product.price_author.data,
            price_part=form.support_product.price_part.data,

            follower=follower, salary_follower=salary_follower,
            copyrighter=copyrighter, salary_copyrighter=salary_copyrighter,
            contenteditor=contenteditor, salary_contenteditor=salary_contenteditor,

            author_id=user_id
        )

        db.session.add(project)
        db.session.commit()
        return redirect(url_for('newproject'))

    return render_template('newproject.html', form=form)



@app.route("/projects/<id_>", methods=["DELETE"])
@login_required
def delete_project(id_):
    project = Project.query.get_or_404(id_)
    try:
        db.session.delete(project)
        db.session.commit()
    except Exception as e:
        return str(e)
    return ''


@app.route("/projects/<id_>", methods=["GET"])
def get_project_by_id(id_):
    try:
        project = Project.query.filter_by(id=id_).first()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


@app.route("/projects/<id_>", methods=["PUT"])
@login_required
def edit_project(id_):
    data = request.get_json()
    try:
        project = Project.query.filter_by(id=id_).first()
        project.name = data["name"]
        db.session.commit()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


@app.route("/projects", methods=["GET"])
def list_projects():
    try:
        projects = Project.query.all()
        return jsonify([e.serialize() for e in projects])
    except Exception as e:
        return str(e)


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = SelectForm()

    if form.validate_on_submit():
        if form.authorinfo.data:
            return redirect(url_for('authorform'))
        elif form.partinfo.data:
            return redirect(url_for('partform'))
        elif form.newproject.data:
            return redirect(url_for('newproject'))

    return render_template('dashboard.html', form=form)


@app.route('/newproject', methods=['GET', 'POST'])
@login_required
def newproject():
    return render_template('newproject.html')

@app.route('/authorform', methods=['GET', 'POST'])
@login_required
def authorform():
    form = AuthorForm()
    if form.validate_on_submit():
        user_id = current_user.get_id()
        newinfo = AuthorInfo(about_me=form.about_me.data, my_goal=form.my_goal.data, author_id=user_id)
        db.session.add(newinfo)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('authorform.html', form=form)


@app.route('/partform', methods=['GET', 'POST'])
@login_required
def partform():
    form = ParticipantForm()
    if form.validate_on_submit():
        user_id = current_user.get_id()
        newinfo = ParticipantInfo(my_skills=form.my_skills.data, my_experience=form.my_experience.data, author_id=user_id)
        db.session.add(newinfo)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('authorform.html', form=form)


if __name__ == '__main__':
    app.run()