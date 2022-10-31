import sys
sys.path.append('./PYHTONEX')

from Conexion import Conexion
from ContratoPersona import ContratoPersona
from logger_base import log 
from CursorDelPool import CursorDelPool

class ContratoPersonaDao:
    _SELECT     = 'SELECT * FROM contrato_persona ORDER BY id'
    _INSERTAR   = 'INSERT INTO contrato_persona(idcontrato, idpersona) VALUES(%s,%s)' 
    _COSTO      = 'SELECT SUM(c.costo) as suma FROM contrato_persona as cp INNER JOIN contrato as c ON c.idcontrato = cp.idcontrato INNER JOIN persona as p ON p.idpersona = cp.idpersona WHERE p.correo = %s'
    _CONTRATO   = 'SELECT p.nombre, c.nocontrato, c.costo FROM contrato_persona as cp INNER JOIN contrato as c ON c.idcontrato = cp.idcontrato INNER JOIN persona as p ON p.idpersona = cp.idpersona WHERE p.correo = %s'

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

    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
                valores = (contrato.idcontrato, contrato.idpersona)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se registro un contrato de personas")
                return cursor.rowcount

    @classmethod
    def costo(cls,correo):
        with CursorDelPool() as cursor:
            valores = (correo,)
            cursor.execute(cls._COSTO, valores)
            registros = cursor.fetchall()
            return registros
    
    @classmethod
    def contrato(cls,correo):
        with CursorDelPool() as cursor:
            valores = (correo,)
            cursor.execute(cls._CONTRATO, valores)
            registros = cursor.fetchall()
            return registros

if __name__ == "__main__":

    #INSERT
    # contrato = ContratoPersona(idpersona=3, idcontrato=2)
    # ContratoRegistrado = ContratoPersonaDao.insertar(contrato)
    # log.debug(f"Clientes registrados {ContratoRegistrado}")

    #SELECT
    contrato = ContratoPersonaDao.seleccionar()
    for p in contrato:
        print(p)

    #CostosporCorreo
    contratoper = ContratoPersonaDao.costo(correo="pp@gmail.com")
    for p in contratoper:
        print('\n')
        print(f'Suma total de costos de contrato es: {p}')

    #Descripción
    contratoper1 = ContratoPersonaDao.contrato(correo="pp@gmail.com")
    for p in contratoper1:
        print('\n')
        print(p)