import psycopg2 as bd
from psycopg2 import pool
import sys
import logging as log
import django as dj
print(dj.get_version())

class Conexion:
    _DATABASE   = 'examenpy'
    _USERNAME   = 'postgres'
    _PWD        = 'admin' 
    _PORT       = '5432'
    _HOST       = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                cls._MIN_CON,
                cls._MAX_CON,
                host = cls._HOST,
                user = cls._USERNAME,
                password = cls._PWD,
                port = cls._PORT,
                database = cls._DATABASE)
                log.debug(f'Creacion del pool{cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error en el pool{e}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida: {conexion}')
        return conexion


    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Conexion regresada: {conexion}')


    @classmethod
    def cerrarConexiones(cls) :
        cls.obtenerPool().closeall()    


if __name__ == '__main__':
    Conexion.obtenerConexion()
    print("Se obtuvo conexion")















"""
Backup Conexion, Este codigo lo cambiamos en clase el dia 6/10/22
"""
# import psycopg2 as db
# import sys
# # import logger_base as log
# import logging as log

# class Conexion:
#     _DATABASE   = 'test_db'
#     _USERNAME   = 'postgres'
#     _PWD        = 'admin' 
#     _DBPORT     = '5432'
#     _HOST       = '127.0.0.1'

#     _conexion = None
#     _cursor = None

# # cls = class conexion puede ser cualquiera.
#     @classmethod 
#     def ObtenerConexion(cls):
#         if cls._conexion is None:
#             try:
#                 cls._conexion = db.connect( host = cls._HOST, user = cls._USERNAME, password = cls._PWD, port = cls._DBPORT, database = cls._DATABASE)
#                 log.debug(f"Conexion a la bd: {cls._conexion}")      
#             except Exception as e:
#                 log.debug(f"Ocurrio un error: {e}")
#                 sys.exit()
#         else:
#             return cls._conexion


#     @classmethod
#     def ObtenerCursor(cls):
#         if cls._cursor is None:
#             try:
#                 cls._cursor = cls.ObtenerConexion().cursor()
#                 print(cls._cursor)
#                 log.debug(f"Conexion a la bd: {cls._conexion}")          
#                 return cls._cursor
#             except Exception as e:
#                 log.debug(f"Ocurrio un error: {e}")
#                 sys.exit
#         else:
#             return cls._cursor

            
# if __name__ == '__main__':
#     Conexion.ObtenerConexion()
#     Conexion.ObtenerCursor()

