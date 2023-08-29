from flaskr import create_app
from .modelos import db, Cancion,Usuario,Album,Medio
from flask_restful import Api
from .vistas import vista_canciones , vista_cancion , vista_usuarios , vista_usuario , vista_albumes, vista_album

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
# inicio de api
api = Api(app)
#ruta de la vista que quiero consultar el parametro la clase a usar y la ruta tiene tanto get como post
api.add_resource(vista_canciones,'/canciones')
api.add_resource(vista_cancion,'/canciones/<int:id>')

#ruta usuario
api.add_resource(vista_usuarios,'/usuarios')
api.add_resource(vista_usuario,'/usuarios/<int:id>')

# ruta album
api.add_resource(vista_albumes,'/albumes')
api.add_resource(vista_album,'/albumes/<int:id>')
