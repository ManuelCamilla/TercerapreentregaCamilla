from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")



def hogar(request):
    return render(request, "aplicacion/hogar.html")

def ropa(request):
    return render(request, "aplicacion/entregables.html")

def clientes(request):
    ctx = {"clientes": Cliente.objects.all() }
    return render(request, "aplicacion/clientes.html", ctx)

def clienteForm(request):
    if request.method == "POST":                
        cliente = Cliente(nombre=request.POST['nombre'], comision=request.POST['comision'])
        cliente.save()
        return HttpResponse("Se grabo con exito el cliente!")
    
    return render(request, "aplicacion/clienteForm.html")

def clienteForm2(request):
    if request.method == "POST":   
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get('nombre')
            cliente_id = miForm.cleaned_data.get('comision')
            cliente = cliente(nombre=cliente_nombre, id=cliente_id)
            cliente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm2.html", {"form":miForm})

def buscarComision(request):
    return render(request, "aplicacion/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        clientes = Cliente.objects.filter(comision__icontains=comision)
        return render(request, 
                      "aplicacion/resultadosComision.html", 
                      {"comision": comision, "clientes":clientes})
    return HttpResponse("No se ingresaron datos para buscar!")


#__________________________________
def juguetes(request):
    ctx = {'juguetes': juguetes.objects.all() }
    return render(request, "aplicacion/juguetes.html", ctx)

def updateJuguete(request, id_juguete):
    juguete = juguete.objects.get(id=id_juguete)
    if request.method == "POST":
        miForm = JugueteForm(request.POST)
        if miForm.is_valid():
            juguete.id = miForm.cleaned_data.get('id')
            juguete.marca = miForm.cleaned_data.get('marca')
            juguete.nombre = miForm.cleaned_data.get('nombre')
            
            juguete.save()
            return redirect(reverse_lazy('juguetes'))   
    else:
        miForm = JugueteForm(initial={'nombre':juguete.nombre, 
                                       'apellido':juguete.apellido, 
                                       'email':juguete.email, 
                                       'profesion':juguete.profesion})         
    return render(request, "aplicacion/jugueteForm.html", {'form': miForm})   

def deletejuguete(request, id_juguete):
    juguete = juguetes.objects.get(id=id_juguete)
    juguete.delete()
    return redirect(reverse_lazy('juguetes'))

def createjuguete(request):    
    if request.method == "POST":
        miForm = JugueteForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_apellido = miForm.cleaned_data.get('apellido')
            p_email = miForm.cleaned_data.get('email')
            p_profesion = miForm.cleaned_data.get('profesion')
            juguete = juguete(nombre=p_nombre, 
                             apellido=p_apellido,
                             email=p_email,
                             profesion=p_profesion,
                             )
            juguete.save()
            return redirect(reverse_lazy('juguetes'))
    else:
        miForm = JugueteForm()

    return render(request, "aplicacion/jugueteForm.html", {"form":miForm})

#______ Class Based View

class HogarList(ListView):
    model = Hogar

class HogarCreate(CreateView):
    model = Hogar
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('hogar')

class HogarDetail(DetailView):
    model = Hogar

class HogarUpdate(UpdateView):
    model = Hogar
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('hogar')    

class HogarDelete(DeleteView):
    model = Hogar
    success_url = reverse_lazy('hogar')    