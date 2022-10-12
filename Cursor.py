from Conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio del Metodo with __enter__")
        self._conexion = Conexion.getConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_detalle):
        log.debug("Se ejecuta metodo __exit__")
        if exc_val:
            self._conexion.rollback()
            log.error(f"Ocurrio una excepcion: {exc_type} {exc_val} {exc_detalle}")
        else:
            self._conexion.commit()
            log.debug("Se termino la transaccion con un commit")
        self._cursor.close()
        Conexion.delConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())



