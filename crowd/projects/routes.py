from flask import jsonify, render_template, url_for, redirect, Blueprint
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


    project.copyrighter = form.copyrighter.data
    project.salary_copyrighter = form.salary_copyrighter.data
    project.videographer = form.videographer.data
    project.salary_videographer = form.salary_videographer.data
    project.director = form.director.data
    project.salary_director = form.salary_director.data
    project.scriptwriter = form.scriptwriter.data
    project.salary_scriptwriter = form.salary_scriptwriter.data
    project.graphicdesigner = form.graphicdesigner.data
    project.salary_graphicdesigner = form.salary_graphicdesigner.data
    project.producer = form.producer.data
    project.salary_producer = form.salary_producer.data
    project.soundengineer = form.soundengineer.data
    project.salary_soundengineer = form.salary_soundengineer.data
    project.lightingtechnician = form.lightingtechnician.data
    project.salary_lightingtechnician = form.salary_lightingtechnician.data
    project.seospecialist = form.seospecialist.data
    project.salary_seospecialist = form.salary_seospecialist.data
    project.communitymanager = form.communitymanager.data
    project.salary_communitymanager = form.salary_communitymanager.data
    project.monetizationspecialist = form.monetizationspecialist.data
    project.salary_monetizationspecialist = form.salary_monetizationspecialist.data

    current_project = CalculateProject(form)
    project.salary_follower, project.total_salary_follower, project.count_followers = current_project.get_salary_follower()
    project.amount_project = current_project.get_fee_amount()
    project.price_product, project.count_product = current_project.get_count_and_price_product()
    project.amount_donate = current_project._amount_project
    project.amount_order_product = current_project._amount_order_product

    if not project.author_id: project.author_id = user_id

    return project

def get_data_rating_project(form, user_id, rating_project):
    current_project = CalculateRatingProject(form)

@projects.route("/newproject", methods=["GET", "POST"])
@login_required
def create_project():
    form = NewProject()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        project = get_data_project(form, user_id, Project())
        #rating = get_data_rating_project(project, user_id, RatingProject())
        db.session.add(project)
        #db.session.add(rating)
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    else:
        # Распечатать ошибки в консоль для отладки
        print(form.errors)

    return render_template('newproject.html', form=form)

@projects.route("/editproject", methods=["GET", "POST"])
@login_required
def edit_project():
    user_id = current_user.get_id()
    project = Project.query.filter_by(author_id=user_id).first()
    form = NewProject(obj=project)  # Передаем объект проекта для предварительного заполнения формы

    if form.validate_on_submit():
        # Проверяем валидность формы
        if project is None:
            # Если проект не существует, создаем новый объект Project
            project = Project(author_id=user_id)
            db.session.add(project)

        # Обновляем данные проекта из формы
        form.populate_obj(project)
        db.session.commit()
        flash('Данные проекта успешно обновлены!', 'success')
        return redirect(url_for('users.dashboard'))

    return render_template('editproject.html', form=form, project=project)


@projects.route("/projects/<id_>", methods=["DELETE"])
@login_required
def delete_project(id_):
    project = Project.query.get_or_404(id_)
    try:
        db.session.delete(project)
        db.session.commit()
    except Exception as e:
        return str(e)
    return ''



@projects.route("/projects/<id_>", methods=["GET", "POST"])
def get_project_by_id(id_):

    join = JoinForm()
    project = Project.query.filter_by(id=id_).first()

    current_user_id = current_user.get_id()
    user = User.query.filter_by(id=current_user_id).first()
    user_profession = user.profession[0]

    join_buttons = {
        'join_copyrighter': 'copyrighter',
        'join_videographer': 'videographer', 'join_director': 'director',
        'join_scriptwriter': 'scriptwriter', 'join_graphicdesigner': 'graphicdesigner',
        'join_producer': 'producer', 'join_soundengineer': 'soundengineer',
        'join_lightingtechnician': 'lightingtechnician', 'join_seospecialist': 'seospecialist',
        'join_communitymanager': 'communitymanager', 'join_monetizationspecialist': 'monetizationspecialist',
    }
    if project.author_id == current_user_id: redirect(url_for('projects.editproject'))
    for user_project in user.participation_projects:
        if user_project == project.id:
            pass # дописать логику потом


    if join.validate_on_submit():
        for button, field in join_buttons.items():
            if getattr(join, button).data and getattr(project, field) > 0:
                setattr(project, field, getattr(project, field) - 1)
                new_match_project = JoinProject(project_id=project.id, **{button: True})
                db.session.add(new_match_project)
                break

        db.session.commit()

    return render_template('project_by_id.html', project=project, join=join, user_profession=user_profession)


@projects.route("/projects", methods=["GET"])
def list_projects():
    try:
        projects = Project.query.all()
        return jsonify([e.serialize() for e in projects])
    except Exception as e:
        return str(e)


@projects.route('/newproject', methods=['GET', 'POST'])
@login_required
def newproject():
    return render_template('newproject.html')