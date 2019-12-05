from flask import flash, redirect,render_template,url_for, request
from flask_login import login_required, login_user,logout_user
from . import auth

#local import
from .. import db
from ..models import Pengguna


@auth.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        periksa_pengguna = Pengguna.query.filter_by(username = request.form['username']).first()
        if periksa_pengguna is not None and periksa_pengguna.verify_password(request.form['password']):
            login_user(periksa_pengguna)
            if periksa_pengguna.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:
            error = "Username tidak dapat ditemukan"
    return render_template('auth/index.html',error = error, title="Login")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('auth.login')
    