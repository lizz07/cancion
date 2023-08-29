from flask_restful import Resource
from ..modelos import db, Cancion, CancionSchema, Usuario, UsuarioSchema, Album, AlbumSchema, Medio, EnumADiccionario
from flask import request

cancion_shema = CancionSchema()
usuario_shema= UsuarioSchema()
album_shema= AlbumSchema()
#new
class vista_canciones(Resource):

    def get(self):
        return[cancion_shema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],\
                                minutos=request.json['minutos'],\
                                segundos=request.json['segundos'],\
                                interprete=request.json['interprete'])

        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_shema.dump(nueva_cancion)


class vista_cancion(Resource):

    def get(self, id):
        return cancion_shema.dump(Cancion.query.get_or_404(id))

    def put(self, id):
        cancion = Cancion.query.get_or_404(id)
        cancion.titulo = request.json.get('titulo',cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)


        db.session.commit()
        return cancion_shema.dump(cancion)


    def delete(self, id):
        cancion = Cancion.query.get_or_404(id)

        db.session.delete(cancion)
        db.session.commit()
        return 'operacion exitosa',204


class vista_usuarios(Resource):

    def get(self):
        return[usuario_shema.dump(Usuario) for Usuario in Usuario.query.all()]

    def post(self):
        nuevo_usuario = Usuario(nombre=request.json['nombre'],\
                                contrasena=request.json['contrasena'])


        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_shema.dump(nuevo_usuario)


class vista_usuario(Resource):

    def get(self, id):
        return usuario_shema.dump(Usuario.query.get_or_404(id))

    def put(self, id):
        usuario = Usuario.query.get_or_404(id)
        usuario.nombre = request.json.get('nombre',usuario.titulo)
        usuario.contrasena = request.json.get('contrasena', usuario.minutos)

        db.session.commit()
        return usuario_shema.dump(usuario)


    def delete(self, id):
        usuario = Usuario.query.get_or_404(id)

        db.session.delete(usuario)
        db.session.commit()
        return 'operacion exitosa',204

class vista_albumes(Resource):

    def get(self):
        return[album_shema.dump(Album) for Album in Album.query.all()]

    def post(self):
        nuevo_album = Album(titulo=request.json['titulo'],\
                            anio=request.json['anio'],\
                            descripcion=request.json['descripcion'],\
                            medio=request.json['medio'])

        db.session.add(nuevo_album)
        db.session.commit()
        return cancion_shema.dump(nuevo_album)

class vista_album(Resource):

    def get(self, id):
        return album_shema.dump(Album.query.get_or_404(id))

    def put(self, id):
        album = Album.query.get_or_404(id)
        album.titulo = request.json.get('titulo',album.titulo)
        album.anio = request.json.get('anio', album.anio)
        album.descripcion = request.json.get('descripcion', album.descripcion)
        album.medio = request.json.get('medio', album.medio)


        db.session.commit()
        return album_shema.dump(album)


    def delete(self, id):
        usuario = Usuario.query.get_or_404(id)

        db.session.delete(usuario)
        db.session.commit()
        return 'operacion exitosa',204

