from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError, Optional
from wtforms import StringField, SubmitField, IntegerField, SelectMultipleField, SelectField


class NewProject(FlaskForm):
    name_blog = StringField(validators=[
        InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "What do we call it?"})
    idea_blog = StringField(validators=[InputRequired(), Length(min=10, max=2000)],
                            render_kw={"placeholder": "Tell us the main idea of your project"})
    topic_blog = SelectField(
        'What is the topic of your blog?', choices=[
            ('fitness', 'fitness'), ('travel', 'travel'), ('fashion', 'fashion'),
            ('finance', 'finance'), ('health', 'health'), ('technology', 'technology'),
            ('family', 'family'), ('home', 'home'), ('books', 'books'), ('arts', 'arts'),
            ('education', 'education'), ('garden', 'garden'), ('games', 'games'),
            ('crafts', 'crafts')
        ])

    name_product = StringField(validators=[
        InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Blog Support Product"})
    price_author = IntegerField('The price of manufacturing the product for the author',
                                [NumberRange(min=0, max=1000000)])

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

    @staticmethod
    def validate_range(form, field):
        if field.data != 0 and not (10000 <= field.data <= 100000):
            raise ValidationError('The salary should be from 10,000 to 100,000 rubles')

    copyrighter = IntegerField(f'How many copyrighter do you need?', validators=[Optional(),
                                                                                 NumberRange(min=0, max=10)])
    salary_copyrighter = IntegerField(f'How much are you willing to pay for a month of work for copyrighter?',
                                      validators=[Optional(), validate_range])

    videographer = IntegerField(f'How many videographer do you need?', [Optional(), NumberRange(min=0, max=10)])
    salary_videographer = IntegerField(f'How much are you willing to pay for a month of work for videographer?',
                                       validators=[Optional(), validate_range])

    director = IntegerField(f'How many director do you need?', [Optional(), NumberRange(min=0, max=10)])
    salary_director = IntegerField(f'How much are you willing to pay for a month of work for director?',
                                   validators=[Optional(), validate_range])

    scriptwriter = IntegerField(f'How many scriptwriter do you need?', [Optional(),
                                                                        NumberRange(min=0, max=10)])
    salary_scriptwriter = IntegerField(f'How much are you willing to pay for a month of work for scriptwriter?',
                                       validators=[Optional(), validate_range])

    graphicdesigner = IntegerField(f'How many graphicdesigner do you need?', [Optional(),
                                                                              NumberRange(min=0, max=10)])
    salary_graphicdesigner = IntegerField(f'How much are you willing to pay for a month of work for graphicdesigner?',
                                          validators=[Optional(), validate_range])

    producer = IntegerField(f'How many producer do you need?', [Optional(), NumberRange(min=0, max=10)])
    salary_producer = IntegerField(f'How much are you willing to pay for a month of work for producer?',
                                   validators=[Optional(), validate_range])

    soundengineer = IntegerField(f'How many soundengineer do you need?', [Optional(),
                                                                          NumberRange(min=0, max=10)])
    salary_soundengineer = IntegerField(f'How much are you willing to pay for a month of work for soundengineer?',
                                        validators=[Optional(), validate_range])

    lightingtechnician = IntegerField(f'How many lightingtechnician do you need?', [Optional(),
                                                                                    NumberRange(min=0, max=10)])
    salary_lightingtechnician = IntegerField(
        f'How much are you willing to pay for a month of work for lightingtechnician?',
        validators=[Optional(), validate_range])

    seospecialist = IntegerField(f'How many seospecialist do you need?', [Optional(),
                                                                          NumberRange(min=0, max=10)])
    salary_seospecialist = IntegerField(f'How much are you willing to pay for a month of work for seospecialist?',
                                        validators=[Optional(), validate_range])

    communitymanager = IntegerField(f'How many communitymanager do you need?', [Optional(),
                                                                                NumberRange(min=0, max=10)])
    salary_communitymanager = IntegerField(f'How much are you willing to pay for a month of work for communitymanager?',
                                           validators=[Optional(), validate_range])

    monetizationspecialist = IntegerField(f'How many monetizationspecialist do you need?', [Optional(),
                                                                                            NumberRange(min=0, max=10)])
    salary_monetizationspecialist = IntegerField(
        f'How much are you willing to pay for a month of work for monetizationspecialist?',
        validators=[Optional(), validate_range])

    submit = SubmitField('public project')


class JoinForm(FlaskForm):
    join_follower = SubmitField('Join!')
    join_copyrighter = SubmitField('Join!')
    join_videographer = SubmitField('Join!')
    join_director = SubmitField('Join!')
    join_scriptwriter = SubmitField('Join!')
    join_graphicdesigner = SubmitField('Join!')
    join_producer = SubmitField('Join!')
    join_soundengineer = SubmitField('Join!')
    join_lightingtechnician = SubmitField('Join!')
    join_seospecialist = SubmitField('Join!')
    join_communitymanager = SubmitField('Join!')
    join_monetizationspecialist = SubmitField('Join!')
