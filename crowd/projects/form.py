from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError
from wtforms import StringField, SubmitField, IntegerField, FormField, SelectMultipleField, SelectField

class SupportProduct(FlaskForm):

    name_product = StringField(validators=[
                            InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Blog Support Product"})
    price_author = IntegerField('The price of manufacturing the product for the author',
                                    [NumberRange(min=0, max=1000000)])


class TeamProject(FlaskForm):

    def __init__(self, *args, **kwargs):
        super(TeamProject, self).__init__(*args, **kwargs)
        self.copyrighter = self.profession_field('copyrighter')
        self.salary_copyrighter = self.salary_field('copyrighter')
        self.videographer = self.profession_field('videographer')
        self.salary_videographer = self.salary_field('videographer')
        self.director = self.profession_field('director')
        self.salary_director = self.salary_field('director')
        self.scriptwriter = self.profession_field('scriptwriter')
        self.salary_scriptwriter = self.salary_field('scriptwriter')
        self.graphicdesigner = self.profession_field('graphicdesigner')
        self.salary_graphicdesigner = self.salary_field('graphicdesigner')
        self.producer = self.profession_field('producer')
        self.salary_producer = self.salary_field('producer')
        self.soundengineer = self.profession_field('soundengineer')
        self.salary_soundengineer = self.salary_field('soundengineer')
        self.lightingtechnician = self.profession_field('lightingtechnician')
        self.salary_lightingtechnician = self.salary_field('lightingtechnician')
        self.seospecialist = self.profession_field('seospecialist')
        self.salary_seospecialist = self.salary_field('seospecialist')
        self.communitymanager = self.profession_field('communitymanager')
        self.salary_communitymanager = self.salary_field('communitymanager')
        self.monetizationspecialist = self.profession_field('monetizationspecialist')
        self.salary_monetizationspecialist = self.salary_field('monetizationspecialist')

    @staticmethod
    def profession_field(label_prefix):
        return IntegerField(f'How many {label_prefix} do you need?', [NumberRange(min=1, max=10)])

    @staticmethod
    def salary_field(label_prefix):
        return IntegerField(
            f'How much are you willing to pay for a month of work for {label_prefix}?', validators=[
                NumberRange(min=10000, max=100000, message="The salary should be from 10,000 to 100,000 rubles"),
                TeamProject.MultipleOf(1000)])
    @staticmethod
    def MultipleOf(multiple_of):
        def _multiple_of(field):
            if field.data % multiple_of != 0:
                raise ValidationError(f"The value must be a multiple of {multiple_of}")
        return _multiple_of

    # copyrighter = profession_field('copyrighter')
    # salary_copyrighter = salary_field('copyrighter')
    #
    # videographer = profession_field('videographer')
    # salary_videographer = salary_field('videographer')
    #
    # director = profession_field('director')
    # salary_director = salary_field('director')
    #
    # scriptwriter = profession_field('scriptwriter')
    # salary_scriptwriter = salary_field('scriptwriter')
    #
    # graphicdesigner = profession_field('graphicdesigner')
    # salary_graphicdesigner = salary_field('graphicdesigner')
    #
    # producer = profession_field('producer')
    # salary_producer = salary_field('producer')
    #
    # soundengineer = profession_field('soundengineer')
    # salary_soundengineer = salary_field('soundengineer')
    #
    # lightingtechnician = profession_field('lightingtechnician')
    # salary_lightingtechnician = salary_field('lightingtechnician')
    #
    # seospecialist = profession_field('seospecialist')
    # salary_seospecialist = salary_field('seospecialist')
    #
    # communitymanager = profession_field('communitymanager')
    # salary_communitymanager = salary_field('communitymanager')
    #
    # monetizationspecialist = profession_field('monetizationspecialist')
    # salary_monetizationspecialist = salary_field('monetizationspecialist')



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
    topic_blog = FormField(TopicsProject)
    support_product = FormField(SupportProduct)
    work_plan = FormField(WorkPlan)
    team_project = FormField(TeamProject)
    submit = SubmitField('public project')




class JoinForm(FlaskForm):
    join_follower = SubmitField('Join!')
    join_copyrighter= SubmitField('Join!')
    join_contenteditor = SubmitField('Join!')



