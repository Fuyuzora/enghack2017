from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class IDForm(Form):
    reddit = StringField('UserID', validators=[DataRequired()])