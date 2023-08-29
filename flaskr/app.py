from flaskr import create_app
from .modelos import db,  Usuario, Album, Medio , Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# Prueba 1
with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Juan Pablo')
    u = Usuario(nombre='juan', contrasena='12345')
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    a.canciones.append(c)
    u.albumes.append(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
