from flaskr import create_app
from .modelos import db, Cancion, Usuario, Medio , Album

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# Prueba 1
with app.app_context():
    c = Cancion(titulo='Prueba',minutos=2,segundos=25,interprete='Juan Pablo')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

# Prueba 2
with app.app_context():
    u = Usuario(nombre='lizz07', contrasena='200469')
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())

# Prueba 3
with app.app_context():
    a = Album(titulo='Álbum de Prueba', anio=2023, descripcion='musica regge', medio=Medio.DISCO)
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())
