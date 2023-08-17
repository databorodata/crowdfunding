from flask import request, jsonify, render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user

from crowd.models import db, Project
from crowd.projects.form import NewProject, JoinForm


projects = Blueprint('projects', __name__)

def get_data_project(form, user_id, project):
    if form.team_project.follower.data: project.follower = form.team_project.follower.data
    if form.team_project.salary_follower.data: project.salary_follower = form.team_project.salary_follower.data
    if form.team_project.copyrighter.data: project.copyrighter = form.team_project.copyrighter.data
    if form.team_project.salary_copyrighter.data: project.salary_copyrighter = form.team_project.salary_copyrighter.data
    if form.team_project.contenteditor.data: project.contenteditor = form.team_project.contenteditor.data
    if form.team_project.salary_contenteditor.data: project.salary_contenteditor = form.team_project.salary_contenteditor.data

    project.name_blog = form.name_blog.data
    project.name_product = form.support_product.name_product.data
    project.product_quantity = form.support_product.product_quantity.data
    project.price_author = form.support_product.price_author.data
    project.price_part = form.support_product.price_part.data

    if not project.author_id:
        project.author_id = user_id

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


@projects.route("/projects/<id_>", methods=["GET"])
def get_project_by_id(id_):
    join = JoinForm()
    project = Project.query.filter_by(id=id_).first()
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

