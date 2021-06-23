from django.shortcuts import render

# Create your views here.
def home (request):
    lista = ["Chocolate", "Protos con Masamorra", "Cazuela"]
    contexto = {
        'nombre' :'Mariapaz Silva',
        'edad':23,
        'comidas': lista
    }
    return render(request,'core/home.html', contexto)
