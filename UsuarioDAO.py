from Cursor import CursorDelPool
from Usuario import Usuario
from logger_base import log


class UsuarioDAO:
    """
    DAO (Data Access Object)
    CRUD (CREATE-READ-UPDATE-DELETE)
    """

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY idusuario'
    _INSERTAR = 'INSERT INTO usuario (username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s , password = %s WHERE idusuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE idusuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertarUsuario(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            values = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, values)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizarUsuario(cls, usuario: Usuario):
        with CursorDelPool() as cursor:
            values = (usuario.username, usuario.password, usuario.idUsuario)
            cursor.execute(cls._ACTUALIZAR, values)
            log.debug(f'Usuario Actualizado Correctamente : {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminarUsuario(cls, idUsuario):
        with CursorDelPool() as cursor:
            values = (idUsuario,)
            cursor.execute(cls._ELIMINAR, values)
            log.debug(f'Usuario Eliminado Correctamente con id : {idUsuario}')
            return cursor.rowcount
