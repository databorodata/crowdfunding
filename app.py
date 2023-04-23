from flask import Flask, request, jsonify
from models import db, Project

import os


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def hello():
    return "Hello DevOps!"


@app.route("/projects", methods=["POST"])
def create_project():
    data = request.get_json()
    try:
        project = Project(name=data["name"])
        db.session.add(project)
        db.session.commit()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


@app.route("/projects/<id_>", methods=["GET"])
def get_project_by_id(id_):
    try:
        project = Project.query.filter_by(id=id_).first()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


@app.route("/projects/<id_>", methods=["PUT"])
def edit_project(id_):
    data = request.get_json()
    try:
        project = Project.query.filter_by(id=id_).first()
        project.name = data["name"]
        db.session.commit()
        return jsonify(project.serialize())
    except Exception as e:
        return str(e)


@app.route("/projects", methods=["GET"])
def list_projects():
    try:
        projects = Project.query.all()
        return jsonify([e.serialize() for e in projects])
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
