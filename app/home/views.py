from flask import redirect, render_template, url_for
from flask_login import login_required

#local import
from . import home


@home.route('/dashborad')
def dashboard():
    return render_template('home/dashboard.html')