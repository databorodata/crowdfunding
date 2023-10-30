from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange
from wtforms import StringField, SubmitField, IntegerField, FormField, SelectMultipleField

class SupportProduct(FlaskForm):

    name_product = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Blog Support Product"})
    product_quantity = IntegerField('How many units of the product will need to be implemented?',
                                    [NumberRange(min=1, max=1000000)])
    price_author = IntegerField('The price of manufacturing the product for the author',
                                    [NumberRange(min=1, max=1000000)])
    price_part = IntegerField('The price of manufacturing a product for a partner',
                                [NumberRange(min=1, max=1000000)])


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


class TopicsProject(FlaskForm):
    topics = SelectMultipleField('What specialties do you own?',
                               choices=[('fitness', 'fitness'), ('travel', 'travel'), ('fashion', 'fashion'),
                                        ('finance', 'finance'), ('health', 'health'), ('technology', 'technology'),
                                        ('family', 'family'), ('home', 'home'), ('books', 'books'), ('arts', 'arts'),
                                        ('education', 'education'), ('garden', 'garden'), ('games', 'games'), ('crafts', 'crafts')])

class NewProject(FlaskForm):

    name_blog = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "What do we call it?"})
    idea_blog = StringField(validators=[
        InputRequired(), Length(min=10, max=2000)], render_kw={"placeholder": "Tell us the main idea of your project"})
    topics_blog = FormField(TopicsProject)
    support_product = FormField(SupportProduct)
    team_project = FormField(TeamProject)
    submit = SubmitField('public project')




class JoinForm(FlaskForm):
    join_follower = SubmitField('Join!')
    join_copyrighter= SubmitField('Join!')
    join_contenteditor = SubmitField('Join!')



