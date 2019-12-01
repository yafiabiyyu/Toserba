from flask import render_template
from flask_login import login_required
from . import auth

@auth.route('/')
def login():
    return render_template('auth/index.html',title='Login')