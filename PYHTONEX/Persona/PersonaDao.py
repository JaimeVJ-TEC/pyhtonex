import sys
sys.path.append('./PYHTONEX')

from Conexion import Conexion
from Persona import Persona
from logger_base import log 
from CursorDelPool import CursorDelPool

class PersonaDao:
    _SELECT  = 'SELECT * FROM persona ORDER BY idpersona'
    _INSERTAR = 'INSERT INTO persona(nombre, edad, correo) VALUES(%s,%s,%s)' 
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, edad=%s,correo=%s WHERE idpersona=%s'
    _ELIMINAR  = 'DELETE FROM persona WHERE idpersona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                personas = []
                for r in registros:
                    persona = Persona(r[0],r[1],r[2],r[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.edad, persona.correo)
                cursor.execute(cls._INSERTAR,valores)
                log.debug("Se inserto una persona")
                return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.edad, persona.correo ,persona.idpersona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug("Se actualizo una persona")
                return cursor.rowcount
                
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
                valores = (persona.idpersona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug("Se elimino una persona")
                return cursor.rowcount

if __name__ == "__main__":

    # Insertar
    # persona = Persona(nombre="Carlos", edad=23, correo="carlos@gmail.com")
    # personasInsertadas = PersonaDao.insertar(persona)
    # log.debug(f"Personas insertadas {personasInsertadas}")


    #Actualizar
    # persona = Persona(nombre="Pepe", edad=27, correo="pp@gmail.com",idpersona=1)
    # personasActualizadas = PersonaDao.actualizar(persona)
    # log.debug(f"Personas actualizadas: {personasActualizadas}")

    # Eliminar
    # persona = Persona(idpersona=2)
    # personasEliminadas = PersonaDao.eliminar(persona)
    # log.debug(f"Personas eliminadas {personasEliminadas}")

    #Ver
    personas = PersonaDao.seleccionar()
    for p in personas:
        print(p)