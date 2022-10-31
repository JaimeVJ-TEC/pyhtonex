from flask import Flask
from models import Empleado,Cliente
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired

class EmpleadoForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    direccion = StringField("Direccion: ", validators=[DataRequired()])
    sueldo = FloatField("Sueldo: ", validators=[DataRequired()])
    enviar = SubmitField("Aceptar")

class ClienteForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    direccion = StringField("Direccion: ", validators=[DataRequired()])
    enviar = SubmitField("Aceptar")