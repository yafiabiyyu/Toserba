from flask import flash, redirect,render_template,url_for, request
from flask_login import login_required, login_user,logout_user
from . import auth

@auth.route('/', methods=['GET', 'POST'])
def login():
    pass