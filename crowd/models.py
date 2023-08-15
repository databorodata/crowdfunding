from flask_login import UserMixin
from crowd import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name_blog = db.Column(db.String, nullable=False)
    name_product = db.Column(db.String, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    price_author = db.Column(db.Integer, nullable=False)
    price_part = db.Column(db.Integer, nullable=False)

    follower = db.Column(db.Integer)
    salary_follower = db.Column(db.Integer)
    copyrighter = db.Column(db.Integer)
    salary_copyrighter = db.Column(db.Integer)
    contenteditor = db.Column(db.Integer)
    salary_contenteditor = db.Column(db.Integer)

    author_id = db.Column(db.Integer, nullable=False)

# class Project(db.Model):
#     __tablename__ = 'projects'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     author = db.Column(db.Integer, nullable=False)
#
#     def __init__(self, name: str, author: int) -> None:
#         self.name = name
#         self.author = author
#
#     def __repr__(self) -> str:
#         return f"<id {self.id}>"
#
#     def serialize(self) -> dict:
#         return {
#             'id': self.id,
#             'name': self.name,
#             'author': self.author
#         }



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    my_skills = db.Column(db.String(1000), nullable=False)
    my_experience = db.Column(db.String(1000), nullable=False)
    copyrighter = db.Column(db.Boolean, nullable=False)
    contenteditor = db.Column(db.Boolean, nullable=False)




class ParticipantInfo(db.Model):
    __tablename__ = 'partinfo'

    id = db.Column(db.Integer, primary_key=True)
    my_skills = db.Column(db.String(1000), nullable=False)
    my_experience = db.Column(db.String(1000), nullable=False)
    copyrighter = db.Column(db.Boolean)
    contenteditor = db.Column(db.Boolean)
    part_id = db.Column(db.Integer, nullable=False)
