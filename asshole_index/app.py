from flask import Flask, render_template, flash, redirect
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object('config')

class IDForm(Form):
    reddit = StringField('UserID', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def redditID():
    form = IDForm()
    if form.validate_on_submit():
        flash('asshole index request for redditID="%s"' % form.reddit.data)
        return redirect('/%s' % form.reddit.data)
    return render_template('index.html',
                           title='enter UserID',
                           form=form,
                           id=form.reddit.data)

@app.route('/<userID>', methods=['GET', 'POST'])
def assholeIndex(userID=None):
    return render_template('asshole_index.html',
                           userID=userID)