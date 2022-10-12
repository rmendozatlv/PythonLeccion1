from Usuario import Usuario

from UsuarioDAO import UsuarioDAO
from logger_base import log
from Cursor import CursorDelPool

print("1. Crear Usuario.")
print("2. Modificar Usuario.")
print("3. Eliminar Usuario.")
print("4. Listar Usuarios.")
print("5 Salir del Sistema.")

ctador = 0
while ctador != 5:
    ctador = int(input("Ingrese las opciones de 1 a 5 para realizar su operacion:"))
    if ctador == 1:
        username = input("Ingrese el username : ")
        password = input("Ingrese el password : ")
        usuario = Usuario(username=username, password=password)
        rows = UsuarioDAO.insertarUsuario(usuario)
        log.debug(f"Usuario Insertado Correctamente: {rows}")

    if ctador == 2:
        idusurio = input("Ingrese el idusuario : ")
        username = input("Ingrese el username : ")
        password = input("Ingrese el password : ")
        usuario = Usuario(idusurio, username, password)
        rows = UsuarioDAO.actualizarUsuario(usuario)
        log.debug(f"Usuario Insertado Correctamente: {rows}")

    if ctador == 3:
        idusurio = input("Ingrese el idusuario : ")
        rows = UsuarioDAO.eliminarUsuario(idusurio)
        log.debug(f"Usuario Eliminado Correctamente: {rows}")

    if ctador == 4:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            print(usuario)

