from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class IntroForm(FlaskForm):
    name = StringField("Hi, what's your name?", validators=[DataRequired()])
