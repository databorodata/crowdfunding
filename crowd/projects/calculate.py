from crowd.projects.form import NewProject
from math import ceil
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
        return self._salary_follower, self._total_salary_follower, self._count_followers

    def get_salary_professionals(self):
        months = self.form.count_months.data
        if type(self.form.copyrighter) == int and type(self.form.salary_copyrighter) == int:
            self._salary_all_professionals += self.form.copyrighter * self.form.salary_copyrighter * months
        if type(self.form.videographer) == int and type(self.form.salary_videographer) == int:
            self._salary_all_professionals += self.form.videographer * self.form.salary_videographer * months
        if type(self.form.director) == int and type(self.form.salary_director) == int:
            self._salary_all_professionals += self.form.director * self.form.salary_director * months
        if type(self.form.scriptwriter) == int and type(self.form.salary_scriptwriter) == int:
            self._salary_all_professionals += self.form.scriptwriter * self.form.salary_scriptwriter * months
        if type(self.form.graphicdesigner) == int and type(self.form.salary_graphicdesigner) == int:
            self._salary_all_professionals += self.form.graphicdesigner * self.form.salary_graphicdesigner * months
        if type(self.form.producer) == int and type(self.form.salary_producer) == int:
            self._salary_all_professionals += self.form.producer * self.form.salary_producer * months
        if type(self.form.soundengineer) == int and type(self.form.salary_soundengineer) == int:
            self._salary_all_professionals += self.form.soundengineer * self.form.salary_soundengineer * months
        if type(self.form.lightingtechnician) == int and type(self.form.salary_lightingtechnician) == int:
            self._salary_all_professionals += self.form.lightingtechnician * self.form.salary_lightingtechnician * months
        if type(self.form.seospecialist) == int and type(self.form.salary_seospecialist) == int:
            self._salary_all_professionals += self.form.seospecialist * self.form.salary_seospecialist * months
        if type(self.form.communitymanager) == int and type(self.form.salary_communitymanager) == int:
            self._salary_all_professionals += self.form.communitymanager * self.form.salary_communitymanager * months
        if type(self.form.monetizationspecialist) == int and type(self.form.salary_monetizationspecialist) == int:
            self._salary_all_professionals += self.form.monetizationspecialist * self.form.salary_monetizationspecialist * months
        return self._salary_all_professionals

    def get_fee_amount(self):
        if not self._amount_project:
            self.get_salary_professionals()
            self.get_salary_follower()
            self._amount_project = self._salary_all_professionals + self._total_salary_follower
        return self._amount_project

    def get_count_and_price_product(self):
        if not self._amount_project: self._amount_project = self.get_fee_amount()
        cost_price = self.form.price_author.data
        self._price_product = ceil(cost_price * 0.2) + cost_price
        self._count_product = self._amount_project // ceil(cost_price * 0.2) + 1
        return  self._price_product, self._count_product



class CalculateRatingProject:

    def __init__(self, form):
        self.form = form

