from crowd.projects.form import NewProject
from math import ceil
class CalculateProject:

    def __init__(self, form):
        self._optimal_count_months = 6
        self._optimal_count_sites = 5
        self._optimal_count_posts = 10
        self._salary_follower = 1500
        self._count_followers = 100
        self._salary_all_professionals = 0
        self._amount_project = None
        self._total_salary_follower = None
        self._price_product = None
        self.form = NewProject()

    def get_salary_follower(self):
        ratio_posts, ratio_moths, ratio_sites = 1, 1, 1
        ratio_moths -= (self._optimal_count_months - self.form.work_plan.count_months.data) / 10
        ratio_sites -= (self._optimal_count_sites - len(self.form.work_plan.placement_sites.data)) / 10
        ratio_posts -= (self._optimal_count_posts - self.form.work_plan.count_posts.data) / 20
        self._salary_follower = int(self._salary_follower * ratio_posts * ratio_sites)
        self._total_salary_follower = int(self._salary_follower * self._count_followers * ratio_moths * ratio_posts * ratio_sites)
        return self._salary_follower, self._total_salary_follower, self._count_followers

    def get_salary_professionals(self):
        months = self.form.work_plan.count_months.data
        step, one_professional = False, 0
        for v in self.form.team_project.data.values():
            print(v, type(v), self.form.team_project.data)
            if step and type(v) == int:
                self._salary_all_professionals += one_professional * months * v
                step = False
            elif not step and type(v) == int:
                one_professional += v
                step = True
        return self._salary_all_professionals

    def get_fee_amount(self):
        if not self._amount_project:
            self.get_salary_professionals()
            self.get_salary_follower()
            self._amount_project = self._salary_all_professionals + self._total_salary_follower
        return self._amount_project

    def get_count_and_price_product(self):
        if not self._amount_project: self._amount_project = self.get_fee_amount()
        cost_price = self.form.support_product.price_author.data
        self._price_product = ceil(cost_price * 0.2) + cost_price
        self._count_product = self._amount_project // ceil(cost_price * 0.2) + 1
        return  self._price_product, self._count_product
