from crowd.projects.form import NewProject
from math import ceil
from crowd import db
from sqlalchemy import text

class CalculateProject:

    def __init__(self, form):
        self.form = form
        self._optimal_count_months = 6
        self._optimal_count_sites = 5
        self._optimal_count_posts = 10
        self._salary_follower = 1500
        self._count_followers = 100
        self._salary_all_professionals = 0
        self._amount_project = None
        self._total_salary_follower = None
        self._price_product = None
        self._amount_donate = 0
        self._amount_order_product = 0

    def get_salary_follower(self):
        ratio_posts, ratio_moths, ratio_sites = 1, 1, 1
        ratio_moths -= (self._optimal_count_months - self.form.count_months.data) / 10
        ratio_sites -= (self._optimal_count_sites - len(self.form.placement_sites.data)) / 10
        ratio_posts -= (self._optimal_count_posts - self.form.count_posts.data) / 20
        self._salary_follower = int(self._salary_follower * ratio_posts * ratio_sites)
        self._total_salary_follower = int(self._salary_follower * self._count_followers * ratio_moths * ratio_posts * ratio_sites)

    def get_salary_professionals(self):
        months = self.form.count_months.data
        def multiplication(a, b, c):
            if isinstance(a, int) and isinstance(b, int) and isinstance(c, int): return a * b * c
            else: return 0

        self._salary_all_professionals += \
            multiplication(self.form.copyrighter.data, self.form.salary_copyrighter.data, months) + \
            multiplication(self.form.videographer.data, self.form.salary_videographer.data, months) + \
            multiplication(self.form.director.data, self.form.salary_director.data, months) + \
            multiplication(self.form.scriptwriter.data, self.form.salary_scriptwriter.data, months) + \
            multiplication(self.form.graphicdesigner.data, self.form.salary_graphicdesigner.data, months) + \
            multiplication(self.form.producer.data, self.form.salary_producer.data, months) + \
            multiplication(self.form.soundengineer.data, self.form.salary_soundengineer.data, months) + \
            multiplication(self.form.lightingtechnician.data, self.form.salary_lightingtechnician.data, months) + \
            multiplication(self.form.seospecialist.data, self.form.salary_seospecialist.data, months) + \
            multiplication(self.form.communitymanager.data, self.form.salary_communitymanager.data, months) + \
            multiplication(self.form.monetizationspecialist.data, self.form.salary_monetizationspecialist.data, months)

    def get_count_and_price_product(self):
        if not self._amount_project: self._amount_project = self.calculate_project()
        cost_price = self.form.price_author.data
        self._price_product = ceil(cost_price * 0.2) + cost_price
        self._count_product = self._amount_project // ceil(cost_price * 0.2) + 1

    def calculate_project(self):
        if not self._amount_project:
            self.get_salary_professionals()
            self.get_salary_follower()
            self._amount_project = self._salary_all_professionals + self._total_salary_follower
            self.get_count_and_price_product()



class CalculateRatingProject:

    def __init__(self, project):
        self.project = project
        self._norm_salary_follower = 1500
        self._rating_followers = None
        self._rating_specialists = None
        self._rating_promotion = 1.0
        self._rating_overall = None
        self._count_specialists = 0


    def get_rating_followers(self):
        self._rating_followers = (self.project.count_months / 12) + \
                            (self.project.salary_follower / 3000) + \
                           (1 - (self.project.count_followers / 100))

    def get_rating_specialists(self):
        project_id = self.project.id
        query = text(
            """
            SELECT (copyrighter + videographer + director + scriptwriter + graphicdesigner + 
                    producer + soundengineer + lightingtechnician + seospecialist + 
                    communitymanager + monetizationspecialist) AS total_specialists
            FROM projects
            WHERE projects.id = :project_id
            """
        )
        result = db.session.execute(query.params(project_id=project_id))
        self._count_specialists = result.scalar()
        if self._count_specialists == None: self._count_specialists = 3
        self._rating_specialists = 15000.0 / (self.project.salary_all_professionals // self._count_specialists)


    def get_rating_promotion(self):
        pass

    def get_rating_overall(self):
        self._rating_overall = self._rating_followers + self._rating_promotion + self._rating_specialists

    def calculate_rating(self):
        self.get_rating_promotion()
        self.get_rating_specialists()
        self.get_rating_followers()
        self.get_rating_overall()