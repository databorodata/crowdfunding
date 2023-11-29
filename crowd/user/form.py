from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectMultipleField
from crowd.models import User


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    @staticmethod
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError('That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    remember = BooleanField("Запомнить", default=False)
    submit = SubmitField('Login')


class SelectForm(FlaskForm):
    partinfo = SubmitField('Edit information about yourself')
    editproject = SubmitField('Edit your project')
    newproject = SubmitField('Create your project')


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
        choices=[
            ('copyrighter', 'copyrighter'), ('videographer', 'videographer'), ('director', 'director'),
            ('scriptwriter', 'scriptwriter'), ('graphicdesigner', 'graphicdesigner'), ('producer', 'producer'),
            ('soundengineer', 'soundengineer'), ('lightingtechnician', 'lightingtechnician'),
            ('seospecialist', 'seospecialist'), ('communitymanager', 'communitymanager'),
            ('monetizationspecialist', 'monetizationspecialist')
        ])
    topics_user = SelectMultipleField('What topics are you interested in?',
                                      choices=[('fitness', 'fitness'), ('travel', 'travel'), ('fashion', 'fashion'),
                                               ('finance', 'finance'), ('health', 'health'),
                                               ('technology', 'technology'),
                                               ('family', 'family'), ('home', 'home'), ('books', 'books'),
                                               ('arts', 'arts'),
                                               ('education', 'education'), ('garden', 'garden'), ('games', 'games'),
                                               ('crafts', 'crafts')])

    submit = SubmitField('add')
