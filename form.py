from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm, Form
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField


class HomeForm(FlaskForm):
    registration = SubmitField('register')
    authentication = SubmitField('enter')


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


class SelectForm(FlaskForm):
    authorinfo = SubmitField('author form')
    partinfo = SubmitField('part form')
    newproject = SubmitField('new project')


class AuthorForm(FlaskForm):

    about_me = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "About me"})
    my_goal = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My goal"})
    submit = SubmitField('add/edit')


class NewProject(FlaskForm):

    name_blog = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "what do we call it?"})
    amount = IntegerField('The required amount', [validators.NumberRange(min=4, max=12)])




class ParticipantForm(FlaskForm):
    my_skills = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My skills"})
    my_experience = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My experience"})
    submit = SubmitField('add')