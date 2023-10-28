from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from crowd.config import ProductionConfig

db = SQLAlchemy()
bcrypt = Bcrypt()



login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(ProductionConfig)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from crowd.main.routes import main
    from crowd.user.routes import users
    from crowd.projects.routes import projects
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(projects)

    return app
