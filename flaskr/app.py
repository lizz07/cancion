from flaskr import create_app
from .modelos import db,  Usuario, Album, Medio , Cancion
from .modelos import AlbumSchema
app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# Prueba 1
with app.app_context():
    Album_Schema=AlbumSchema()
    A = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    db.session.add(A)
    db.session.commit()
    print([Album_Schema.dump(album) for album in Album.query.all()])
