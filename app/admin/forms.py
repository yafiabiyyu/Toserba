from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Optional


class BarangForms(FlaskForm):
    nama_barang = StringField('Nama Barang', validators=[DataRequired()])
    stock_barang = IntegerField(' Stock Barang', validators=[DataRequired()])
    harga_barang = IntegerField('Harga Barang', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PenggunaForms(FlaskForm):
    nama_pengguna = StringField('Nama Pengguna', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    role = SelectField('Role',choices = [('1', 'admin'), ('0', 'staf')], validators=[DataRequired()])
    submit = SubmitField('Submit')
