from django.db import models

class Tratamiento(models.Model):
    nombre=models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    indicaciones = models.CharField(max_length=255)
    duracion= models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Paciente(models.Model):
    numero_segurosocial = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento= models.DateField(auto_now=False)
    telefono = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    tratamiento = models.ForeignKey(Tratamiento,on_delete = models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f'Paciente {self.id} : {self.nombre}: {self.apellidos}'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    clasificación = models.CharField(max_length=255)
    caducidad= models.DateField(auto_now=False)
    almacenamiento = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Proveedor,on_delete = models.SET_NULL,null=True)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} \n Fecha de caducidad: {self.caducidad}'

class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento= models.DateField(auto_now=False)
    numero_cedulaprofesional = models.CharField(max_length=255)
    numero_segurosocial = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'{self.id}.- {self.nombre}: {self.apellidos}'
