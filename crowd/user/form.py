from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError, NumberRange
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FormField, SelectMultipleField
from crowd.models import User



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
    partinfo = SubmitField('Edit information about yourself')
    editproject = SubmitField('Edit your project')
    newproject = SubmitField('Create your project')


class AuthorForm(FlaskForm):

    about_me = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "About me"})
    my_goal = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My goal"})
    submit = SubmitField('add/edit')


class SupportProduct(FlaskForm):

    name_product = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Blog Support Product"})
    product_quantity = IntegerField('How many units of the product will need to be implemented?',
                                    [NumberRange(min=1, max=1000000)])
    price_author = IntegerField('The price of manufacturing the product for the author',
                                    [NumberRange(min=1, max=1000000)])
    price_part = IntegerField('The price of manufacturing a product for a partner',
                                [NumberRange(min=1, max=1000000)])

class ParticipantForm(FlaskForm):
    my_skills = StringField(
        validators=[InputRequired(), Length(min=1, max=1000)],
        render_kw={"placeholder": "My skills"}
    )
    my_experience = StringField(
        validators=[InputRequired(), Length(min=1, max=1000)],
        render_kw={"placeholder": "My experience"}
    )
    profession = SelectMultipleField(
        'What specialties do you own?',
        choices=[('copyrighter', 'copyrighter'), ('videographer', 'videographer'), ('director', 'director'),
            ('scriptwriter', 'scriptwriter'), ('graphicdesigner', 'graphicdesigner'), ('producer', 'producer'),
            ('soundengineer', 'soundengineer'), ('lightingtechnician', 'lightingtechnician'),
            ('seospecialist', 'seospecialist'), ('communitymanager', 'communitymanager'),
                 ('monetizationspecialist', 'monetizationspecialist')])
    submit = SubmitField('add')


class TeamProject(FlaskForm):

    follower = IntegerField('How many followers do you need?',
                                    [NumberRange(min=1, max=1000000)])
    salary_follower = IntegerField('How much are you willing to pay?',
                                    [NumberRange(min=1, max=1000000)])

    #follower = FormField(Follower, validators=[custom_validator])
    copyrighter = IntegerField('How many copyrighter do you need?',
                                    [NumberRange(min=1, max=1000000)])
    salary_copyrighter = IntegerField('How much are you willing to pay?',
                                    [NumberRange(min=1, max=1000000)])

    contenteditor = IntegerField('How many contenteditor do you need?',
                                    [NumberRange(min=1, max=1000000)])
    salary_contenteditor = IntegerField('How much are you willing to pay?',
                                    [NumberRange(min=1, max=1000000)])


class NewProject(FlaskForm):

    name_blog = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "What do we call it?"})
    support_product = FormField(SupportProduct)
    team_project = FormField(TeamProject)
    submit = SubmitField('public project')





