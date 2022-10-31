import sys
sys.path.append('./PYHTONEX')

from Conexion import Conexion
from ContratoPersona import ContratoPersona
from logger_base import log 
from CursorDelPool import CursorDelPool

class ContratoPersonaDao:
    _SELECT     = 'SELECT * FROM contrato_persona ORDER BY id'
    _INSERTAR   = 'INSERT INTO contrato_persona(idcontrato, idpersona) VALUES(%s,%s)' 

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                contratos = []
                for r in registros:
                    contrato = ContratoPersona(r[0],r[1],r[2])
                    contratos.append(contrato)
                return contratos

    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
                valores = (contrato.idcontrato, contrato.idpersona)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se registro un contrato de personas")
                return cursor.rowcount


if __name__ == "__main__":

    #INSERT
    contrato = ContratoPersona(idpersona=1, idcontrato=1)
    ContratoRegistrado = ContratoPersonaDao.insertar(contrato)
    log.debug(f"Clientes registrados {ContratoRegistrado}")

    #SELECT
    contrato = ContratoPersonaDao.seleccionar()
    for p in contrato:
        print(p)