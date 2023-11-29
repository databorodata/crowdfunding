from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user

from crowd.models import db, Project, JoinProject, RatingProject, User
from crowd.projects.form import NewProject, JoinForm
from crowd.projects.calculate import CalculateProject, CalculateRatingProject
from flask import flash

projects = Blueprint('projects', __name__)


def get_data_project(form, user_id, project):
    project.name_blog = form.name_blog.data
    project.idea_blog = form.idea_blog.data

    project.topic_blog = [form.topic_blog.data]

    project.name_product = form.name_product.data
    project.price_author = form.price_author.data

    project.count_posts = form.count_posts.data
    project.placement_sites = form.placement_sites.data
    project.count_months = form.count_months.data

    project.copyrighter = form.copyrighter.data or 0
    project.salary_copyrighter = form.salary_copyrighter.data or 0
    project.videographer = form.videographer.data or 0
    project.salary_videographer = form.salary_videographer.data or 0
    project.director = form.director.data or 0
    project.salary_director = form.salary_director.data or 0
    project.scriptwriter = form.scriptwriter.data or 0
    project.salary_scriptwriter = form.salary_scriptwriter.data or 0
    project.graphicdesigner = form.graphicdesigner.data or 0
    project.salary_graphicdesigner = form.salary_graphicdesigner.data or 0
    project.producer = form.producer.data or 0
    project.salary_producer = form.salary_producer.data or 0
    project.soundengineer = form.soundengineer.data or 0
    project.salary_soundengineer = form.salary_soundengineer.data or 0
    project.lightingtechnician = form.lightingtechnician.data or 0
    project.salary_lightingtechnician = form.salary_lightingtechnician.data or 0
    project.seospecialist = form.seospecialist.data or 0
    project.salary_seospecialist = form.salary_seospecialist.data or 0
    project.communitymanager = form.communitymanager.data or 0
    project.salary_communitymanager = form.salary_communitymanager.data or 0
    project.monetizationspecialist = form.monetizationspecialist.data or 0
    project.salary_monetizationspecialist = form.salary_monetizationspecialist.data or 0

    current_project = CalculateProject(form)
    current_project.calculate_project()
    project.amount_project = current_project._amount_project
    project.salary_follower = current_project._salary_follower
    project.total_salary_follower = current_project._total_salary_follower
    project.count_followers = current_project._count_followers
    project.salary_all_professionals = current_project._salary_all_professionals
    project.price_product = current_project._price_product
    project.count_product = current_project._count_product
    project.amount_donate = current_project._amount_donate
    project.amount_order_product = current_project._amount_order_product

    if not project.author_id:
        project.author_id = user_id

    return project


def get_data_rating_project(project):
    current_calculate = CalculateRatingProject(project)
    current_calculate.calculate_rating()
    current_rating = RatingProject()
    current_rating.project_id = project.id
    current_rating.rating_overall = round(float(current_calculate._rating_overall), 3)
    current_rating.rating_followers = round(float(current_calculate._rating_followers), 3)
    current_rating.rating_promotion = round(float(current_calculate._rating_promotion), 3)
    current_rating.rating_specialists = round(float(current_calculate._rating_specialists), 3)
    return current_rating


@projects.route("/newproject", methods=["GET", "POST"])
@login_required
def create_project():
    form = NewProject()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        try:
            project = get_data_project(form, user_id, Project())
            db.session.add(project)

            rating = get_data_rating_project(project)
            db.session.add(rating)

            db.session.commit()

            return redirect(url_for('users.dashboard'))
        except Exception as e:
            db.session.rollback()  # Если произойдет ошибка, откатываем транзакцию
            print(f"Error: {e}")
    else:
        print(form.errors)

    return render_template('newproject.html', form=form)


@projects.route("/editproject", methods=["GET", "POST"])
@login_required
def edit_project():
    user_id = current_user.get_id()
    project = Project.query.filter_by(author_id=user_id).first()
    form = NewProject(obj=project)

    if form.validate_on_submit():
        try:
            project = Project(author_id=user_id)
            db.session.add(project)
            form.populate_obj(project)
            rating = get_data_rating_project(project)
            db.session.add(rating)
            db.session.commit()
            flash('Данные проекта успешно обновлены!', 'success')
            return redirect(url_for('users.dashboard'))
        except Exception as e:
            db.session.rollback()  # Если произойдет ошибка, откатываем транзакцию
            print(f"Error: {e}")
    else:
        print(form.errors)

    return render_template('editproject.html', form=form, project=project)


@projects.route("/projects/<id_>", methods=["GET", "POST"])
def get_project_by_id(id_):
    join = JoinForm()
    project = Project.query.filter_by(id=id_).first()

    current_user_id = current_user.get_id()
    user = User.query.filter_by(id=current_user_id).first()
    if user and user.profession:
        user_profession = user.profession[0]
    else:
        user_profession = None

    join_buttons = {
        'join_copyrighter': 'copyrighter',
        'join_videographer': 'videographer', 'join_director': 'director',
        'join_scriptwriter': 'scriptwriter', 'join_graphicdesigner': 'graphicdesigner',
        'join_producer': 'producer', 'join_soundengineer': 'soundengineer',
        'join_lightingtechnician': 'lightingtechnician', 'join_seospecialist': 'seospecialist',
        'join_communitymanager': 'communitymanager', 'join_monetizationspecialist': 'monetizationspecialist',
    }
    if current_user_id and project.author_id == current_user_id: redirect(url_for('projects.editproject'))
    if user and user.participation_projects:
        for user_project in user.participation_projects:
            if user_project == project.id:
                pass  # дописать логику потом

    if join.validate_on_submit():
        for button, field in join_buttons.items():
            if getattr(join, button).data and getattr(project, field) > 0:
                setattr(project, field, getattr(project, field) - 1)
                new_match_project = JoinProject(project_id=project.id, **{button: True})
                db.session.add(new_match_project)
                break

        db.session.commit()

    return render_template(
        'project_by_id.html',
        project=project,
        join=join,
        user_profession=user_profession)
