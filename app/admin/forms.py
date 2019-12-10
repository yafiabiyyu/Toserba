from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class BarangForms(FlaskForm):
    nama_barang = StringField('Nama Barang', validators=[DataRequired()])
    stock_barang = IntegerField(' Stock Barang', validators=[DataRequired()])
    harga_barang = IntegerField('Harga Barang', validators=[DataRequired()])
    submit = SubmitField('Submit')