from django.shortcuts import render,get_object_or_404,redirect
from gestorapp.models import Medicamento
from gestorapp.forms import MedicamentoForm


def detalleMedicamento(request,id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    return render(request,'./Medicamento/detalleMedicamento.html',{'medicamento' :medicamento})

def agregarMedicamento(request):
    if request.method =="POST":
        formaMedicamento = MedicamentoForm(request.POST)
        if formaMedicamento.is_valid():
            formaMedicamento.save()
            return redirect('medicamento')
    else:
        formaMedicamento=MedicamentoForm()
        return render(request,'./Medicamento/agregarMedicamento.html',{'formaMedicamento':formaMedicamento})

def editarMedicamento(request,id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    if request.method == "POST":
        formaMedicamento= MedicamentoForm(request.POST,instance=medicamento)
        if formaMedicamento.is_valid():
            formaMedicamento.save()
            return redirect('medicamento')
    else:
        formaMedicamento=MedicamentoForm(instance=medicamento)
        return render(request,'./Medicamento/editarMedicamento.html',{'formaMedicamento':formaMedicamento})

def eliminarMedicamento(request,id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    if (medicamento):
        medicamento.delete()
    return redirect('medicamento')