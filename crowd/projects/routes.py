from flask import request, jsonify, render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user

from crowd.models import db, Project
from crowd.projects.form import NewProject


projects = Blueprint('projects', __name__)

@projects.route("/newproject", methods=["GET", "POST"])
@login_required
def create_project():
    form = NewProject()
    user_id = current_user.get_id()
    if form.validate_on_submit():
        follower = form.team_project.follower.data
        salary_follower = form.team_project.salary_follower.data
        copyrighter = form.team_project.copyrighter.data
        salary_copyrighter = form.team_project.salary_copyrighter.data
        contenteditor = form.team_project.contenteditor.data
        salary_contenteditor = form.team_project.salary_contenteditor.data

        project = Project(
            name_blog=form.name_blog.data,
            name_product=form.support_product.name_product.data,
            product_quantity=form.support_product.product_quantity.data,
            price_author=form.support_product.price_author.data,
            price_part=form.support_product.price_part.data,

            follower=follower, salary_follower=salary_follower,
            copyrighter=copyrighter, salary_copyrighter=salary_copyrighter,
            contenteditor=contenteditor, salary_contenteditor=salary_contenteditor,

            author_id=user_id
        )

        db.session.add(project)
        db.session.commit()
        return redirect(url_for('newproject'))

    return render_template('newproject.html', form=form)



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
    try:
        project = Project.query.filter_by(id=id_).first()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


@projects.route("/projects/<id_>", methods=["PUT"])
@login_required
def edit_project(id_):
    data = request.get_json()
    try:
        project = Project.query.filter_by(id=id_).first()
        project.name = data["name"]
        db.session.commit()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


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

