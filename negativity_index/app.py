from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from .reddit_user import User


app = Flask(__name__)
app.config.from_object('config')

class IDForm(FlaskForm):
    reddit = StringField('username', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def reddit_username():
    form = IDForm()
    if form.is_submitted():
        return redirect(url_for('assholeIndex', username=form.reddit.data))
    return render_template('index.html',
                           title='enter username',
                           form=form)

@app.route('/<username>', methods=['GET', 'POST'])
def assholeIndex(username=None):
    rate = User.rate_of_negativeness(username)
    return render_template('asshole_index.html',
                           username=username, rateOfNegativeness=rate)