from logger_base import log
from Conexion import Conexion


class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        log.debug("Inicio Metodo With")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self,tipo_exeption, valor_exeption, detalle_exeption):
        log.debug("Se ejecuta exit")
        if valor_exeption:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM contrato_personas")
        log.debug(cursor.fetchall())
        
