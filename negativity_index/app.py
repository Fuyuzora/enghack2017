from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from reddit_user import User

app = Flask(__name__)
app.config.from_object('config')

class IDForm(FlaskForm):
    reddit = StringField('username', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def reddit_username():
    form = IDForm()
    if form.is_submitted():
        return redirect(url_for('negativity_index', username=form.reddit.data))
    return render_template('index.html',
                           title='enter username',
                           form=form)

@app.route('/<username>', methods=['GET', 'POST'])
def negativity_index(username=None):
    percent = User.rate_of_negativeness(username)*100

    if percent <= 10:
        detailed_descrip = "Trustworthy"
    else:
        detailed_descrip = "Possible Troll" #Robert



    precent_str = "%f %%" % percent
    # python bug
    ## rate = User.rate_of_negativeness(username)
    ## precent_str = "%f %%" % precent*100
    return render_template('asshole_index.html',
                           username=username,
                           rateOfNegativeness=precent_str,
                           description=detailed_descrip)