from django.shortcuts import render

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()

# Create your views here.
def home (request):
    lista = ["Chocolate", "Protos con Masamorra", "Cazuela"]

    hijo = Persona ("Valentin Olivares", '2')

    contexto = {
        'nombre' :'Mariapaz Silva',
        'edad':23,
        'comidas': lista,
        'hijo': hijo 
    }
    return render(request,'core/home.html', contexto)
