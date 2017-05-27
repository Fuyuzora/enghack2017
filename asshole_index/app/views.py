from flask import render_template, flash, redirect
from app import app
from .forms import IDForm

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