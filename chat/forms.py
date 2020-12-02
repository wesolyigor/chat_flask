# name room submit
# na stronie głownej ma być formularz, jeśli jest poprawnie wypełniony
# to mamy dodać nazwę i i mie do sesji i zalogować go
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField(label='Write name of your task', validators=[DataRequired()])
    room = StringField(label='Room:', validators=[DataRequired()])
    submit = SubmitField(label='LOGIN.', validators=[DataRequired()])
