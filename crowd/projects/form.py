from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError, Optional
from wtforms import StringField, SubmitField, IntegerField, FormField, SelectMultipleField, SelectField

class SupportProduct(FlaskForm):

    name_product = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Blog Support Product"})
    price_author = IntegerField('The price of manufacturing the product for the author',
                                    [NumberRange(min=0, max=1000000)])


class TeamProject(FlaskForm):

    copyrighter = IntegerField(f'How many copyrighter do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_copyrighter = IntegerField(f'How much are you willing to pay for a month of work for copyrighter?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    videographer = IntegerField(f'How many videographer do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_videographer = IntegerField(f'How much are you willing to pay for a month of work for videographer?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    director = IntegerField(f'How many director do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_director = IntegerField(f'How much are you willing to pay for a month of work for director?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    scriptwriter = IntegerField(f'How many scriptwriter do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_scriptwriter = IntegerField(f'How much are you willing to pay for a month of work for scriptwriter?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    graphicdesigner = IntegerField(f'How many graphicdesigner do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_graphicdesigner = IntegerField(f'How much are you willing to pay for a month of work for graphicdesigner?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    producer = IntegerField(f'How many producer do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_producer = IntegerField(f'How much are you willing to pay for a month of work for producer?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    soundengineer = IntegerField(f'How many soundengineer do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_soundengineer = IntegerField(f'How much are you willing to pay for a month of work for soundengineer?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    lightingtechnician = IntegerField(f'How many lightingtechnician do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_lightingtechnician = IntegerField(f'How much are you willing to pay for a month of work for lightingtechnician?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    seospecialist = IntegerField(f'How many seospecialist do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_seospecialist = IntegerField(f'How much are you willing to pay for a month of work for seospecialist?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    communitymanager = IntegerField(f'How many communitymanager do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_communitymanager = IntegerField(f'How much are you willing to pay for a month of work for communitymanager?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])

    monetizationspecialist = IntegerField(f'How many monetizationspecialist do you need?', [Optional(), NumberRange(min=1, max=10)])
    salary_monetizationspecialist = IntegerField(f'How much are you willing to pay for a month of work for monetizationspecialist?',
    validators=[Optional(), NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles")])


class TopicsProject(FlaskForm):
    topics = SelectField('What is the topic of your blog?',
                               choices=[('fitness', 'fitness'), ('travel', 'travel'), ('fashion', 'fashion'),
                                        ('finance', 'finance'), ('health', 'health'), ('technology', 'technology'),
                                        ('family', 'family'), ('home', 'home'), ('books', 'books'), ('arts', 'arts'),
                                        ('education', 'education'), ('garden', 'garden'), ('games', 'games'), ('crafts', 'crafts')])

class WorkPlan(FlaskForm):
    count_posts = IntegerField('How many posts are you willing to post per month?', validators=[
                NumberRange(min=1, max=100, message="You must post at least one post per month")])
    placement_sites = SelectMultipleField(
        'What resources are you planning to post content on?',
        choices=[
            ('YouTube', 'YouTube'), ('VK', 'VK'), ('X', 'X'), ('WordPress', 'WordPress'), ('LinkedIn', 'LinkedIn'),
            ('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Tumblr', 'Tumblr'),
            ('LiveJournal', 'LiveJournal'), ('RuTube', 'RuTube'), ('Wix', 'Wix')])
    count_months = IntegerField('How many months will it take you to reach payback?', validators=[
                NumberRange(min=3, max=12, message="Not less than three months and not more than one year")])

class NewProject(FlaskForm):

    name_blog = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "What do we call it?"})
    idea_blog = StringField(validators=[
        InputRequired(), Length(min=10, max=2000)], render_kw={"placeholder": "Tell us the main idea of your project"})
    topic_blog = SelectField('What is the topic of your blog?',
                         choices=[('fitness', 'fitness'), ('travel', 'travel'), ('fashion', 'fashion'),
                                  ('finance', 'finance'), ('health', 'health'), ('technology', 'technology'),
                                  ('family', 'family'), ('home', 'home'), ('books', 'books'), ('arts', 'arts'),
                                  ('education', 'education'), ('garden', 'garden'), ('games', 'games'),
                                  ('crafts', 'crafts')])

    support_product = FormField(SupportProduct)
    work_plan = FormField(WorkPlan)
    team_project = FormField(TeamProject)
    submit = SubmitField('public project')




class JoinForm(FlaskForm):
    join_follower = SubmitField('Join!')
    join_copyrighter= SubmitField('Join!')
    join_contenteditor = SubmitField('Join!')



