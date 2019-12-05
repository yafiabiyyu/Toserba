from flask import redirect, render_template, url_for, abort
from flask_login import login_required, current_user

#local import
from . import home


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/dashboard_admin.html')


@home.route('/dashboard')
def dashboard():
    return render_template('home/dashboard.html')