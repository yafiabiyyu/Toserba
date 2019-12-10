from flask import redirect, render_template, url_for, abort, request, flash
from flask_login import login_required,current_user

from . import admin
from ..models import Barang
from .. import db

def check_admin():
    if not current_user.is_admin:
        abort(403)

@admin.route('/admin/data/barang', methods=['GET','POST'])
@login_required
def data_barang():
    check_admin()
    listBarang = Barang.query.all()
    return render_template('admin/barang/list_barang.html',barang=listBarang,title="Data Barang")



@admin.route('/admin/barang/add', methods=['GET','POST'])
@login_required
def add_barang():
    check_admin()
    add_barang = True
    if request.method == 'POST':
        addbarang = Barang(
            nama_barang = request.form['nama_barang'],
            stock_barang = request.form['stock_barang'],
            harga_barang = request.form['harga_barang']
        )
        try:
            db.session.add(addbarang)
            db.session.commit()
        except:
            #kasih menampilkan error
            pass
        return redirect(url_for('admin.data_barang'))
    return render_template('admin/barang/barangs.html', action="Add",
    add_barang = add_barang, title="Add Data Barang")