from django.shortcuts import render, redirect, get_object_or_404
from .models import Control
from .forms import ControlForm
from django.http import JsonResponse

# Create your views here.
def crear_control(request):
    if request.method == 'POST':
        form = ControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controls')
    else:
        form = ControlForm()

    return render(request, 'control/crear_control.html', {
        'title': 'Crear Control',
        'form': form
    })

def mostrar_controles(request):
    controles = Control.objects.all()
    return render(request, 'control/controls.html', {
        'title': 'Controles',
        'controles': controles
        })

def cambiar_estado(request, control_id):
    control = get_object_or_404(Control, id=control_id)
    control.estado = not control.estado  # Cambia el estado al contrario (True a False, False a True)
    control.save()
    return redirect('controls')  # Redirige de nuevo a la página de controles

def borrarControl(request, id):
    control = Control.objects.get(pk=id)
    control.delete()

    return redirect('controls')

def obtener_estado_control(request, control_nombre):
    control = get_object_or_404(Control, nombre=control_nombre)
    estado = control.estado
    return JsonResponse({'nombre': control.nombre, 'estado': estado})
