from flask_sqlalchemy import SQLAlchemy
import enum
db = SQLAlchemy()


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Enum(Medio))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    __table_args__ = (db.UniqueConstraint('usuario', 'titulo', name='titulo_unico_album'),)
    canciones = db.relationship('Cancion',secondary='album_cancion', back_populates='id_Album')

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    id_Album = db.relationship('Album',secondary='album_cancion', back_populates='canciones')

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    contrasena = db.Column(db.String(128))
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')




albumes_canciones = db.Table('album_cancion', \
    db.Column('album_id',db.Integer, db.ForeignKey('album.id'), primary_key=True),\
    db.Column('cancion_id',db.Integer, db.ForeignKey('cancion.id'), primary_key=True))
