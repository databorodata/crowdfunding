from flask import jsonify, render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user

from crowd.models import db, Project, JoinProject
from crowd.projects.form import NewProject, JoinForm
from crowd.projects.calculate import CalculateProject


projects = Blueprint('projects', __name__)

def get_data_project(form, user_id, project):

    project.name_blog = form.name_blog.data
    project.idea_blog = form.idea_blog.data

    project.topic_blog = [form.topic_blog.data]

    project.name_product = form.support_product.name_product.data
    project.price_author = form.support_product.price_author.data

    project.count_posts = form.work_plan.count_posts.data
    project.placement_sites = form.work_plan.placement_sites.data
    project.count_months = form.work_plan.count_months.data


    project.copyrighter = form.team_project.copyrighter.data
    project.salary_copyrighter = form.team_project.salary_copyrighter.data
    project.videographer = form.team_project.videographer.data
    project.salary_videographer = form.team_project.salary_videographer.data
    project.director = form.team_project.director.data
    project.salary_director = form.team_project.salary_director.data
    project.scriptwriter = form.team_project.scriptwriter.data
    project.salary_scriptwriter = form.team_project.salary_scriptwriter.data
    project.graphicdesigner = form.team_project.graphicdesigner.data
    project.salary_graphicdesigner = form.team_project.salary_graphicdesigner.data
    project.producer = form.team_project.producer.data
    project.salary_producer = form.team_project.salary_producer.data
    project.soundengineer = form.team_project.soundengineer.data
    project.salary_soundengineer = form.team_project.salary_soundengineer.data
    project.lightingtechnician = form.team_project.lightingtechnician.data
    project.salary_lightingtechnician = form.team_project.salary_lightingtechnician.data
    project.seospecialist = form.team_project.seospecialist.data
    project.salary_seospecialist = form.team_project.salary_seospecialist.data
    project.communitymanager = form.team_project.communitymanager.data
    project.salary_communitymanager = form.team_project.salary_communitymanager.data
    project.monetizationspecialist = form.team_project.monetizationspecialist.data
    project.salary_monetizationspecialist = form.team_project.salary_monetizationspecialist.data

    current_project = CalculateProject(form)
    project.salary_follower, project.total_salary_follower, project.count_followers = current_project.get_salary_follower()
    project.amount_project = current_project.get_fee_amount()
    project.price_product, project.count_product = current_project.get_count_and_price_product()

    if not project.author_id: project.author_id = user_id

    return project

@projects.route("/newproject", methods=["GET", "POST"])
@login_required
def create_project():
    form = NewProject()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        project = get_data_project(form, user_id, Project())
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    else:
        # Распечатать ошибки в консоль для отладки
        print(form.errors)

    return render_template('newproject.html', form=form)

@projects.route("/editproject", methods=["GET", "POST"])
@login_required
def edit_project():
    form = NewProject()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        project = Project.query.filter_by(author_id=user_id).first()
        get_data_project(form, user_id, project)
        db.session.commit()
        return redirect(url_for('users.dashboard'))

    return render_template('editproject.html', form=form)


#     return render_template('newproject.html', form=form)


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
    user_exists = JoinProject.query.filter_by(project_id=project.id, user_id=current_user_id).first()

    if project.id != current_user_id and user_exists == None:
        if join.validate_on_submit():

            if join.join_follower.data and project.quantity_follower:
                project.quantity_follower -= 1
                new_match_project = JoinProject(project_id=project.id, user_id=current_user_id, join_follower=True)
                db.session.add(new_match_project)
            elif join.join_copyrighter.data and project.join_copyrighter:
                project.quantity_copyrighter -= 1
                new_match_project = JoinProject(project_id=project.id, user_id=current_user_id, join_copyrighter=True)
                db.session.add(new_match_project)
            elif join.join_contenteditor.data and project.join_contenteditor:
                project.quantity_copyrighter -= 1
                new_match_project = JoinProject(project_id=project.id, user_id=current_user_id, join_contenteditor=True)
                db.session.add(new_match_project)

            db.session.commit()

    return render_template('project_by_id.html', project=project, join=join)


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