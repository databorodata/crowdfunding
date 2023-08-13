from flask_wtf import FlaskForm
from wtforms import SubmitField

class HomeForm(FlaskForm):
    registration = SubmitField('register')
    authentication = SubmitField('enter')

