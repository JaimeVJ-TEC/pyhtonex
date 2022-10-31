from django.shortcuts import render
from gestorapp.models import *
# Create your views here.

def Bienvenida(request):
    return render(request,'index.html')

def VerMedicamento(request):
    medicamentos = Medicamento.objects.order_by('id')
    return render(request,'indexMedicamento.html',{'medicamentos' : medicamentos})

def VerMedico(request):
    medicos = Medico.objects.order_by('id')
    return render(request,'indexMedico.html',{'medicos' : medicos})

def VerPaciente(request):
    pacientes = Paciente.objects.order_by('id')
    return render(request,'indexPaciente.html',{'pacientes' : pacientes})