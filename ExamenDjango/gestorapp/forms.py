from django.forms import ModelForm,EmailInput,DateInput
from gestorapp.models import *

class PacienteForm(ModelForm):
    class Meta:
        model=Paciente
        fields= '__all__'
        widgets= {
            'fecha_nacimiento': DateInput(attrs={'type':'date'}),
            'correo_electronico': EmailInput(attrs={'type':'email'})
        }

class MedicamentoForm(ModelForm):
    class Meta:
        model=Medicamento
        fields= '__all__'
        widgets= {
            'caducidad': DateInput(attrs={'type':'date'})
        }

class MedicoForm(ModelForm):
    class Meta:
        model=Medico
        fields= '__all__'
        widgets= {
            'fecha_nacimiento': DateInput(attrs={'type':'date'})
        }