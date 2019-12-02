from flask import flash, redirect,render_template,url_for, request
from flask_login import login_required, login_user,logout_user
from . import auth

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        periksa_pengguna = Pengguna.query.filter_by(username=request.form['username']).first()
        if periksa_pengguna is not None and periksa_pengguna.verify_password(request.form['password']):
            login_user('periksa_pengguna')
            return redirect(url_for('cashier.dashboard'))
        else:
            return redirect(url_for('auth.login'))
    return render_template('auth/index.html', title="Login")