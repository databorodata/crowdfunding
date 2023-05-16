from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

from models import db, Project, User, RegisterForm, LoginForm

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

@app.route("/")
def hello():
    return "Hello DevOps!"


@app.route("/projects", methods=["POST"])
def create_project():
    data = request.get_json()
    try:
        project = Project(name=data["name"])
        db.session.add(project)
        db.session.commit()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)



@app.route("/projects/<id_>", methods=["DELETE"])
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





@app.route('/')
def home():
    return render_template('home.html')


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


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


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



if __name__ == '__main__':
    app.run()