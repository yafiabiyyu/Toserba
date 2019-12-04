from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Pengguna(db.Model, UserMixin):
    __tablename__ = 'm_pengguna'
    id = db.Column(db.Integer, primary_key=True)
    nama_pengguna = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    transaksi = db.relationship('Transaksi', backref='m_pengguna', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<Pengguna: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return Pengguna.query.get(int(user_id))


class Barang(db.Model):
    __tablename__ = 'barang'
    id = db.Column(db.Integer, primary_key=True)
    nama_barang = db.Column(db.String(50), nullable=False, unique=True)
    stock_barang = db.Column(db.Integer, nullable= False)
    harga_barang = db.Column(db.Integer, nullable= False)
    detail_transaksi = db.relationship('DetailTransaksi', backref='barang', lazy='dynamic')

    def __repr__(self):
        return '<Barang: {}>'.format(self.nama_barang)


class Transaksi(db.Model):
    __tablename__ = 'transaksi'
    id = db.Column(db.String(11),primary_key= True, autoincrement=False)
    id_pegawai = db.Column(db.Integer, db.ForeignKey('m_pengguna.id'), nullable= False)
    tgl_transaksi = db.Column(db.Date, nullable= False)
    jumlah_total = db.Column(db.Integer, nullable= False)
    detail_transaksi = db.relationship('DetailTransaksi', backref='transaksi', lazy='dynamic')

class DetailTransaksi(db.Model):
    __tablename__ = 'detail_transaksi'
    id = db.Column(db.String(8), primary_key=True, autoincrement=False)
    id_transaksi = db.Column(db.String(11),db.ForeignKey('transaksi.id'), nullable=False)
    id_barang = db.Column(db.Integer, db.ForeignKey('barang.id'), nullable= False)
    jumlah_barang = db.Column(db.Integer, nullable=False)
    harga_barang = db.Column(db.Integer, nullable=False)
