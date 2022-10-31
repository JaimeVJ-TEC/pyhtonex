from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.models import Paciente
from gestorapp.forms import PacienteForm


def detallePaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    return render(request,'./Paciente/detallePaciente.html',{'paciente' :paciente})

def agregarPaciente(request):
    if request.method =="POST":
        formaPaciente = PacienteForm(request.POST)
        if formaPaciente.is_valid():
            formaPaciente.save()
            return redirect('paciente')
    else:
        formaPaciente=PacienteForm()
        return render(request,'./Paciente/agregarPaciente.html',{'formaPaciente':formaPaciente})

def editarPaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == "POST":
        formaPaciente= PacienteForm(request.POST,instance=paciente)
        if formaPaciente.is_valid():
            formaPaciente.save()
            return redirect('paciente')
    else:
        formaPaciente=PacienteForm(instance=paciente)
        return render(request,'./Paciente/editarPaciente.html',{'formaPaciente':formaPaciente})

def eliminarPaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    if (paciente):
        paciente.delete()
    return redirect('paciente')