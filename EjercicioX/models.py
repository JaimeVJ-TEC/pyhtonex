from serializer import Serializer
from app import db

class Automovil(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(250))
    costo = db.Column(db.Float)
    def __repr__(self):
        return (f'ID:{self.id},{self.modelo}')


class Empleado(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    direccion = db.Column(db.String(250))
    sueldo = db.Column(db.Float)

    def __repr__(self):
        return (f'ID:{self.id},{self.nombre}')

class Locales(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(250))
    ciudad = db.Column(db.String(250))

    def __repr__(self):
        return (f'ID:{self.id},{self.ciudad}')

class Cliente(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    direccion = db.Column(db.String(250))

    def __repr__(self):
        return (f'ID:{self.id},{self.nombre}')

class Gerente(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    direccion = db.Column(db.String(250))

    def __repr__(self):
        return (f'ID:{self.id},{self.nombre}')