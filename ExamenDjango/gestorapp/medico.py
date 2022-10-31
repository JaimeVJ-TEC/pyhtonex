from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.models import Medico
from gestorapp.forms import MedicoForm


def detalleMedico(request,id):
    medico = get_object_or_404(Medico, pk=id)
    return render(request,'./Medico/detallemedico.html',{'medico' :medico})

def agregarMedico(request):
    if request.method =="POST":
        formaMedico = MedicoForm(request.POST)
        if formaMedico.is_valid():
            formaMedico.save()
            return redirect('medico')
    else:
        formaMedico=MedicoForm()
        return render(request,'./Medico/agregarMedico.html',{'formaMedico':formaMedico})

def editarMedico(request,id):
    medico = get_object_or_404(Medico, pk=id)
    if request.method == "POST":
        formaMedico= MedicoForm(request.POST,instance=medico)
        if formaMedico.is_valid():
            formaMedico.save()
            return redirect('medico')
    else:
        formaMedico=MedicoForm(instance=medico)
        return render(request,'./Medico/editarMedico.html',{'formaMedico':formaMedico})

def eliminarMedico(request,id):
    medico = get_object_or_404(Medico, pk=id)
    if (medico):
        medico.delete()
    return redirect('medico')