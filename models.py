from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"<id {self.id}>"

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
        }
