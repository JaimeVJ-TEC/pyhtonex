import sys
sys.path.append('./PYHTONEX')
from Contrato import Contrato
from logger_base import log
from CursorDelPool import CursorDelPool

class ContratoDao:
    _SELECT     = 'SELECT * FROM contrato ORDER BY idcontrato'
    _INSERTAR   = 'INSERT INTO contrato(nocontrato, costo, fechainicio, fechafin) VALUES(%s,%s,%s,%s)' 
    _ACTUALIZAR = 'UPDATE contrato SET nocontrato=%s, costo=%s, fechainicio=%s, fechafin=%s WHERE idcontrato=%s'
    _ELIMINAR   = 'DELETE FROM contrato WHERE idcontrato=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                contratos = []
                for r in registros:
                    contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                    contratos.append(contrato)
                return contratos

    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
                valores = (contrato.nocontrato, contrato.costo, contrato.fechainicio, contrato.fechafin)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se registro un contrato")
                return cursor.rowcount

    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
                valores = (contrato.nocontrato, contrato.costo, contrato.fechainicio, contrato.fechafin, contrato.idcontrato)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug("Se actualizo un contrato")
                return cursor.rowcount
                
    @classmethod
    def eliminar(cls,contrato):
        with CursorDelPool() as cursor:
                valores = (contrato.idcontrato,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug("Se elimino un contrato")
                return cursor.rowcount

if __name__ == "__main__":

    #INSERT
    # contrato = Contrato(nocontrato=2, costo=220, fechainicio="01/01/22", fechafin="30/12/22")
    # ContratoRegistrado = ContratoDao.insertar(contrato)
    # log.debug(f"Contratos registrados {ContratoRegistrado}")

    #UPDATE
    # contrato = Contrato(nocontrato=5, costo=500, fechainicio="1/06/22", fechafin="10/12/22",idcontrato=1)
    # contratoActualizado = ContratoDao.actualizar(contrato)
    # log.debug(f"Contrato actualizados: {contratoActualizado}")

    # #DELETE
    # contrato = Contrato(idcontrato=3)
    # contratoEliminado = ContratoDao.eliminar(contrato)
    # log.debug(f"Contratos eliminados {contratoEliminado}")

    #SELECT
    contrato = ContratoDao.seleccionar()
    for p in contrato:
        print(p)