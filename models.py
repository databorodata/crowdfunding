from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

db = SQLAlchemy()


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, author: int) -> None:
        self.name = name
        self.author = author

    def __repr__(self) -> str:
        return f"<id {self.id}>"

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author
        }

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)



class AuthorInfo(db.Model):
    __tablename__ = 'authorinfo'

    id = db.Column(db.Integer, primary_key=True)
    about_me = db.Column(db.String(1000), nullable=False)
    my_goal = db.Column(db.String(1000), nullable=False)
    author_id = db.Column(db.Integer, nullable=False)



class ParticipantInfo(db.Model):
    __tablename__ = 'partinfo'

    id = db.Column(db.Integer, primary_key=True)
    my_skills = db.Column(db.String(1000), nullable=False)
    my_experience = db.Column(db.String(1000), nullable=False)
    part_id = db.Column(db.Integer, nullable=False)
