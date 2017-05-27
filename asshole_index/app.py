from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')

class IDForm(FlaskForm):
    reddit = StringField('UserID', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def redditID():
    form = IDForm()
    if form.is_submitted():
        return redirect(url_for('assholeIndex', userID=form.reddit.data))
    return render_template('index.html',
                           title='enter UserID',
                           form=form)

@app.route('/<userID>', methods=['GET', 'POST'])
def assholeIndex(userID=None):
    return render_template('asshole_index.html',
                           userID=userID)