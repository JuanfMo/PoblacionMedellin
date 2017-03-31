from django.shortcuts import render
from .forms import PoblacionForm
from .models import Poblacion

# Create your views here.
def agregar(request):

    if request.method == 'POST':

        form = PoblacionForm(request.POST)

        var_comuna = request.POST.get('comuna', '')
        var_edad = request.POST.get('edad', '')
        var_poblacion_año = request.POST.get('poblacion_año', '')
        var_numero_poblacion = request.POST.get('numero_poblacion', '')

        poblacion_obj = Poblacion(comuna=var_comuna, edad=var_edad, poblacion_año=var_poblacion_año, numero_poblacion=var_numero_poblacion)
        poblacion_obj.save()

        return render(request, 'poblacion/agregar.html', {'poblacion_obj': poblacion_obj})
    else:
        form = PoblacionForm()
        return render(request, 'poblacion/agregar.html', {'form': form})


def mostrar(request):
    all_poblacion = Poblacion.objects.order_by('comuna')
    return render(request, 'poblacion/index.html', {'all_poblacion': all_poblacion})
