from flask import Flask
from crowd.models import User, Project, RatingProject
from crowd import db, bcrypt
from random import choice, randrange
from crowd.projects.calculate import CalculateProject, CalculateRatingProject
from crowd.projects.form import NewProject



def generate_users(app):
    with app.app_context():
        with app.test_request_context('/'):
            for i in range(1, 500):
                topic_list = ['fitness', 'travel', 'fashion', 'finance', 'health',
                              'technology', 'family', 'home', 'books', 'arts',
                              'education', 'garden', 'games', 'crafts']
                nums_topic = randrange(2, 6)
                topic_for_user = set()
                for _ in range(nums_topic): topic_for_user.add(choice(topic_list))
                topic_for_user = list(topic_for_user)

                username = f'user{i}_{randrange(10000)}'  # Добавляем уникальный идентификатор
                password = f'password{i}'
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                new_user = User(username=username,
                                password=hashed_password,
                                profession=[choice(('copyrighter', 'videographer', 'director', 'scriptwriter',
                                                    'graphicdesigner', 'producer', 'soundengineer', 'lightingtechnician',
                                                    'seospecialist', 'communitymanager', 'monetizationspecialist'))],
                                my_skills=f'my_skills{i}',
                                my_experience=f'my_experience{i}',
                                topics_user=topic_for_user)
                db.session.add(new_user)

                sites = ['YouTube', 'VK', 'X', 'WordPress', 'LinkedIn',
                         'Instagram', 'Facebook', 'Tumblr', 'LiveJournal',
                         'RuTube', 'Wix']
                nums_site = randrange(4, 9)
                site_for_project = set()
                for _ in range(nums_site): site_for_project.add(choice(sites))
                site_for_project = list(site_for_project)

                name_blog = f'name blog 1{i}'
                idea_blog = f'idea blog {i}'

                topic_blog = [choice((['fitness', 'travel', 'fashion', 'finance', 'health',
                                        'technology', 'family', 'home', 'books', 'arts',
                                        'education', 'garden', 'games', 'crafts']))]
                name_product = f'name product {i}'
                price_author = randrange(800, 6700)

                count_posts = randrange(3, 27)
                placement_sites = site_for_project
                count_months = randrange(3, 11)

                copyrighter, salary_copyrighter = randrange(2), 0
                if copyrighter: salary_copyrighter = randrange(11000, 26000)

                videographer, salary_videographer = randrange(2), 0
                if videographer: salary_videographer = randrange(11000, 26000)

                director, salary_director = randrange(2), 0
                if director: salary_director = randrange(11000, 26000)

                scriptwriter, salary_scriptwriter = randrange(2), 0
                if scriptwriter: salary_scriptwriter = randrange(11000, 26000)

                graphicdesigner, salary_graphicdesigner = randrange(2), 0
                if graphicdesigner: salary_graphicdesigner = randrange(11000, 26000)

                producer, salary_producer = randrange(2), 0
                if producer: salary_producer = randrange(11000, 26000)

                soundengineer, salary_soundengineer = randrange(2), 0
                if soundengineer: salary_soundengineer = randrange(11000, 26000)

                lightingtechnician, salary_lightingtechnician = randrange(2), 0
                if lightingtechnician: salary_lightingtechnician = randrange(11000, 26000)

                seospecialist, salary_seospecialist = randrange(2), 0
                if seospecialist: salary_seospecialist = randrange(11000, 26000)

                communitymanager, salary_communitymanager = randrange(2), 0
                if communitymanager: salary_communitymanager = randrange(11000, 26000)

                monetizationspecialist, salary_monetizationspecialist = randrange(2), 0
                if monetizationspecialist: salary_monetizationspecialist = randrange(11000, 26000)

                form_project = NewProject()
                generating_data = {
                    'name_blog': name_blog, 'idea_blog': idea_blog, 'topic_blog': topic_blog,
                    'name_product': name_product, 'price_author': price_author,
                    'count_posts': count_posts, 'placement_sites': placement_sites,
                    'count_months': count_months,
                    'copyrighter': copyrighter, 'salary_copyrighter': salary_copyrighter,
                    'videographer': videographer, 'salary_videographer': salary_videographer,
                    'director': director, 'salary_director': salary_director,
                    'scriptwriter': scriptwriter, 'salary_scriptwriter': salary_scriptwriter,
                    'graphicdesigner': graphicdesigner, 'salary_graphicdesigner': salary_graphicdesigner,
                    'producer': producer, 'salary_producer': salary_producer,
                    'soundengineer': soundengineer, 'salary_soundengineer': salary_soundengineer,
                    'lightingtechnician': lightingtechnician, 'salary_lightingtechnician': salary_lightingtechnician,
                    'seospecialist': seospecialist, 'salary_seospecialist': salary_seospecialist,
                    'communitymanager': communitymanager, 'salary_communitymanager': salary_communitymanager,
                    'monetizationspecialist': monetizationspecialist, 'salary_monetizationspecialist': salary_monetizationspecialist
                }

                form_project.process(data=generating_data)

                current_project = CalculateProject(form_project)
                current_project.calculate_project()
                amount_project = current_project._amount_project
                salary_follower = current_project._salary_follower
                total_salary_follower = current_project._total_salary_follower
                count_followers = current_project._count_followers
                salary_all_professionals = current_project._salary_all_professionals
                price_product = current_project._price_product
                count_product = current_project._count_product
                amount_donate = current_project._amount_donate
                amount_order_product = current_project._amount_order_product

                new_project = Project(
                    name_blog=name_blog, idea_blog=idea_blog, topic_blog=topic_blog,
                    name_product=name_product, price_author=price_author,
                    count_posts=count_posts, placement_sites=placement_sites,
                    count_months= count_months,
                    copyrighter = copyrighter, salary_copyrighter=salary_copyrighter,
                    videographer=videographer, salary_videographer=salary_videographer,
                    director=director, salary_director=salary_director,
                    scriptwriter=scriptwriter, salary_scriptwriter=salary_scriptwriter,
                    graphicdesigner=graphicdesigner, salary_graphicdesigner=salary_graphicdesigner,
                    producer=producer, salary_producer=salary_producer,
                    soundengineer=soundengineer, salary_soundengineer=salary_soundengineer,
                    lightingtechnician=lightingtechnician, salary_lightingtechnician=salary_lightingtechnician,
                    seospecialist=seospecialist, salary_seospecialist=salary_seospecialist,
                    communitymanager=communitymanager, salary_communitymanager=salary_communitymanager,
                    monetizationspecialist=monetizationspecialist, salary_monetizationspecialist=salary_monetizationspecialist,
                    salary_all_professionals=salary_all_professionals, salary_follower=salary_follower,
                    total_salary_follower=total_salary_follower, count_followers=count_followers,
                    amount_project=amount_project, price_product=price_product,
                    count_product=count_product, amount_donate=amount_donate,
                    amount_order_product=amount_order_product,
                    author_id=i
                )
                db.session.add(new_project)


                current_calculate = CalculateRatingProject(new_project)
                current_calculate.calculate_rating()
                new_project_rating = RatingProject(
                    project_id=i,
                    rating_overall = round(float(current_calculate._rating_overall), 3),
                    rating_followers = round(float(current_calculate._rating_followers), 3),
                    rating_promotion = round(float(current_calculate._rating_promotion), 3),
                    rating_specialists = round(float(current_calculate._rating_specialists), 3)
                )
                db.session.add(new_project_rating)

        db.session.commit()
