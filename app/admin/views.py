from flask import redirect, render_template, url_for, abort, request, flash
from flask_login import login_required,current_user

from . import admin
from .forms import BarangForms, PenggunaForms
from ..models import Barang,Pengguna
from .. import db

def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/admin/data/pengguna', methods=['GET','POST'])
@login_required
def data_pengguna():
    check_admin()
    listPengguna = Pengguna.query.all()
    return render_template('admin/pengguna/list_pengguna.html',pengguna=listPengguna,title="Data Pengguna")


@admin.route('/admin/pengguna/add', methods=['GET','POST'])
@login_required
def add_pengguna():
    check_admin()
    add_pengguna = True
    form = PenggunaForms()
    if form.validate_on_submit():
        pengguna = Pengguna(
            nama_pengguna = form.nama_pengguna.data,
            username = form.username.data,
            password = "1234",
            is_admin = int(form.role.data)
        )
        db.session.add(pengguna)
        db.session.commit()
        return redirect(url_for('admin.data_pengguna'))
    return render_template('admin/pengguna/pengguna.html', action='Edit',add_pengguna=add_pengguna,
    title = "Edit Data Pengguna", form=form)


@admin.route('/admin/pengguna/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_pengguna(id):
    check_admin()
    add_pengguna = False
    getPengguna = Pengguna.query.get_or_404(id)
    form = PenggunaForms(obj=getPengguna)
    if form.validate_on_submit():
        getPengguna.nama_pengguna = form.nama_pengguna.data
        getPengguna.username = form.username.data
        getPengguna.is_admin = int(form.role.data)
        db.session.commit()
        return redirect(url_for('admin.data_pengguna'))
    return render_template('admin/pengguna/pengguna.html', action='Add',add_pengguna=add_pengguna,
    title = "Tambah Data Pengguna", form=form)


@admin.route('/admin/pengguna/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_pengguna(id):
    check_admin()
    hapusPengguna = Pengguna.query.get_or_404(id)
    db.session.delete(hapusPengguna)
    db.session.commit()
    return redirect(url_for('admin.data_pengguna'))
    return render_template(title="Hapus Data Barang")

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
    form = BarangForms()
    if form.validate_on_submit():
        barang = Barang(
            nama_barang = form.nama_barang.data,
            stock_barang = form.stock_barang.data,
            harga_barang = form.harga_barang.data
        )
        try:
            db.session.add(barang)
            db.session.commit()
        except:
            #kasih menampilkan error
            pass
        return redirect(url_for('admin.data_barang'))
    return render_template('admin/barang/barangs.html', action="Add",
    add_barang = add_barang, title="Tambah Data Barang", form=form)



@admin.route('/admin/barang/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_barang(id):
    check_admin()
    add_barang = False
    
    getBarang = Barang.query.get_or_404(id)
    form = BarangForms(obj=getBarang)
    if form.validate_on_submit():
        getBarang.nama_barang = form.nama_barang.data
        getBarang.stock_barang = form.stock_barang.data
        getBarang.harga_barang = form.harga_barang.data
        db.session.commit()
        return redirect(url_for('admin.data_barang'))
    return render_template('admin/barang/barangs.html', action="Edit",
    add_barang = add_barang, title="Ubah Data Barang", form=form)


@admin.route('/admin/barang/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_barang(id):
    check_admin()
    hapusBarang = Barang.query.get_or_404(id)
    db.session.delete(hapusBarang)
    db.session.commit()
    return redirect(url_for('admin.data_barang'))
    return render_template(title="Hapus Data Barang")
