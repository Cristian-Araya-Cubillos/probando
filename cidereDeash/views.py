from django.shortcuts import render
from django.http import HttpResponse
from powerbiclient import Report
from powerbiclient.authentication import DeviceCodeLoginAuthentication
# Create your views here.

def index(request):
	return render(request, 'index.html')

# En otro archivo, por ejemplo, en views.py
from .utils import mi_funcion
import webbrowser

def mi_funcion():
    #divice_auth = DeviceCodeLoginAuthentication()
    # Lógica de la función
    return "Hola desde mi función"

def abrir_link_automaticamente(request):
    # URL para el flujo de autenticación del dispositivo
    url = "https://microsoft.com/devicelogin"
    # Abre automáticamente la URL en una nueva pestaña o ventana del navegador
    webbrowser.open_new_tab(url)

    return HttpResponse("Se ha abierto automáticamente la página de autenticación del dispositivo.")
    
def nombre(request):
    if request.method == 'POST':
        # Llama a tu función sin procesar los campos del formulario
        #divice_auth = DeviceCodeLoginAuthentication()
        resultado = abrir_link_automaticamente(request)

        # Puedes devolver una respuesta HTTP o renderizar una plantilla según tus necesidades
        return HttpResponse(f'Resultado: {resultado}')

    return render(request, 'index.html')


