import psycopg2 as bd
from logger_base import log
import sys
from psycopg2 import pool


class Conexion:
    _DATABASE = 'Demo2'
    _USERNAME = 'postgres'
    _PASSWORD = '123'
    _DBPORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _Pool = None

    @classmethod
    def getPool(cls):
        if cls._Pool is None:
            try:
                cls._Pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._Pool,
                                                      database=cls._DATABASE)
                log.debug(f"Creacion de pooll exitoso: {cls._Pool}")
                return cls._Pool
            except Exception as ex:
                log.error(f"Ocurrio un error al obtener pool de conexion: {ex}")
                sys.exit()
        else:
            return cls._Pool

    @classmethod
    def getConexion(cls):
        conexion = cls.getPool().getconn()
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def delConexion(cls, conexion):
        cls.getPool().putconn(conexion)
        log.debug(F"Liberamos el objeto conexion al pool : {conexion}")

    @classmethod
    def closeConexiones(cls):
        cls.getPool().closeall()
        log.debug(f"Cerrando todas las conexiones")

    # @classmethod
    # def getConexion(cls):
    #     if cls._connection is None:
    #         try:
    #             cls._connection = bd.connect(host=cls._HOST,
    #                                          user=cls._USERNAME,
    #                                          password=cls._PASSWORD,
    #                                          port=cls._DBPORT,
    #                                          database=cls._DATABASE)
    #             log.debug(f'Conexión Exitosas: {cls._connection}')
    #             return cls._connection
    #         except Exception as e:
    #             log.error(f'Ocurrió una exception al obtener la conexión {e}')
    #             sys.exit()
    #     else:
    #         return cls._connection
    #
    # @classmethod
    # def getCursor(cls):
    #     try:
    #         cls._cursor = cls.getConexion().cursor()
    #         log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
    #         return cls._cursor
    #     except Exception as e:
    #         log.error(f'Ocurrió un error {e}')


if __name__ == '__main__':
    conexion = Conexion.getConexion()
    Conexion.delConexion(conexion)
    conexion2 = Conexion.getConexion()
    conexion3 = Conexion.getConexion()
    conexion4 = Conexion.getConexion()
    conexion5 = Conexion.getConexion()
    conexion6 = Conexion.getConexion()

