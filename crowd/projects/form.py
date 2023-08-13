# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm, Form
from wtforms.validators import InputRequired, Length, ValidationError, NumberRange
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FormField, SelectMultipleField
from models import User


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


class SupportProduct(FlaskForm):

    name_product = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Blog Support Product"})
    product_quantity = IntegerField('How many units of the product will need to be implemented?',
                                    [NumberRange(min=1, max=1000000)])
    price_author = IntegerField('The price of manufacturing the product for the author',
                                    [NumberRange(min=1, max=1000000)])
    price_part = IntegerField('The price of manufacturing a product for a partner',
                                [NumberRange(min=1, max=1000000)])


# class Follower(FlaskForm):
#     follower = IntegerField('How many followers do you need?',
#                                     [NumberRange(min=1, max=1000000)])
#     salary_follower = IntegerField('How much are you willing to pay?',
#                                     [NumberRange(min=1, max=1000000)])


# def custom_validator(form, field):
#     if field.follower.data and not field.salary_follower.data:
#         raise ValidationError("oops")
#     if field.salary_follower.data and not field.follower.data:
#         raise ValidationError("oops1")


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

    # def validate_follower(self, field):
    #     print("111")
    #     print(f"{field.data=}, {self.salary_follower.data=}")
    #     if not field.data and self.salary_follower.data:
    #         raise ValidationError("Follower field should be filled")
    #     if field.data and not self.salary_follower.data:
    #         raise ValidationError("Follower salary should be filled")

    # def validate(self, **kwargs):
    #     print('3axodut')
    #     if not super(TeamProject, self).validate(**kwargs):
    #         print("0")
    #         return False
    #     if (self.follower.data and not self.salary_follower.data) or \
    #         (self.copyrighter.data and not self.salary_copyrighter.data) or \
    #         (self.contenteditor.data and not self.contenteditor_salary.data):
    #         print("1")
    #         msg = 'nuxy9'
    #         self.follower.errors.append(msg)
    #         # raise ValidationError(msg)
    #         return False
    #
    #     if (self.salary_follower.data and not self.follower.data) or \
    #         (self.salary_copyrighter.data and not self.copyrighter.data) or \
    #         (self.salary_contenteditor.data and not self.contenteditor.data):
    #         print("2")
    #         msg = 'nuxy9'
    #         self.follower.errors.append(msg)
    #         return False
    #
    #     print("3")
    #     return True


class NewProject(FlaskForm):

    name_blog = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "What do we call it?"})
    support_product = FormField(SupportProduct)
    team_project = FormField(TeamProject)
    submit = SubmitField('public project')


class ProfForm(FlaskForm):
    prof = SelectMultipleField('What specialties do you own?',
                               choices=[('copyrighter', 'copyrighter'), ('contenteditor', 'contenteditor')])


class ParticipantForm(FlaskForm):
    my_skills = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My skills"})
    my_experience = StringField(validators=[
                           InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "My experience"})
    profession = FormField(ProfForm)
    submit = SubmitField('add')



