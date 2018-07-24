from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..users.models import User
from ..email.email import send_email
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # form = NameForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.name.data).first()
    #     if user is None:
    #         user = User(username=form.name.data)
    #         db.session.add(user)
    #         session['known'] = False
    #         if current_app.config['FLASKY_ADMIN']:
    #             send_email(current_app.config['FLASKY_ADMIN'], 'New User',
    #                        'mail/new_user', user=user)
    #     else:
    #         session['known'] = True
    #     session['name'] = form.name.data
    #     return redirect(url_for('.index'))
    return render_template('index.html')
