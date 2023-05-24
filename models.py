from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm, Form
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField

db = SQLAlchemy()


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, author: int) -> None:
        self.name = name
        self.author = author

    def __repr__(self) -> str:
        return f"<id {self.id}>"

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author
        }

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)



class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField('Login')


class SelectInfo(FlaskForm):
    authorinfo = SubmitField('author form')
    partinfo = SubmitField('part form')



class AuthorInfo(db.Model):
    __tablename__ = 'authorinfo'

    id = db.Column(db.Integer, primary_key=True)
    about_me = db.Column(db.String(1000), nullable=False)
    my_goal = db.Column(db.String(1000), nullable=False)
    author_id = db.Column(db.Integer, nullable=False)


class AuthorForm(FlaskForm):

    about_me = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "About me"})
    my_goal = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My goal"})
    submit = SubmitField('add/edit')


class ParticipantForm(FlaskForm):
    my_skills = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My skills"})
    my_experience = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My experience"})
    submit = SubmitField('add')