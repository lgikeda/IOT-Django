import matplotlib
matplotlib.use('Agg')

from django.shortcuts import render, redirect
from .models import Sensor, Medicion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
@receiver(post_save, sender=Medicion)
def check_temperature_and_send_alert(sender, instance, **kwargs):
    if instance.valor >= 40:
        # Enviar alerta por correo electrónico
        send_mail(
            'Alerta de Temperatura',
            'La temperatura ha alcanzado o superado los 50 grados.',
            'luisikeda.desarrollo@gmail.com',  # Cambia esto al remitente deseado
            ['luisikeda.desarrollo@gmail.com'],  # Cambia esto al destinatario deseado
            fail_silently=False,
        )

@csrf_exempt
def recibirDatos(request):
    if request.method == 'POST':
        try:
            # Obtener datos del cuerpo de la solicitud POST en formato JSON
            data = json.loads(request.body.decode('utf-8'))

            # Obtener el nombre del sensor y el valor desde los datos recibidos
            nombre_sensor = data.get('nombre_sensor')
            valor = data.get('valor')

            # Obtener el sensor o crearlo si no existe
            sensor, created = Sensor.objects.get_or_create(title=nombre_sensor)

            # Almacenar el valor en el sensor
            sensor.value = valor
            sensor.save()

            # Verificar si el sensor tiene ya 20 mediciones y eliminar la más antigua si es necesario
            if sensor.mediciones.count() >= 19:
                # Obtener y eliminar la medicion más antigua
                medicion_mas_antigua = sensor.mediciones.earliest('created_at')
                medicion_mas_antigua.delete()
                
            # Crear una nueva instancia de Medicion
            medicion_nueva = Medicion.objects.create(sensor=sensor, valor=valor)

            # Imprimir ID del nuevo objeto Medicion
            print(f"Nueva Medicion ID: {medicion_nueva.id}")

            # # Obtener las IDs de las mediciones excedentes
            # mediciones_excedentes_ids = Medicion.objects.filter(sensor=sensor).order_by('created_at')[:10].values_list('id', flat=True)

            # # Eliminar las mediciones excedentes por IDs
            # Medicion.objects.filter(id__in=mediciones_excedentes_ids).delete()


            # Devolver una respuesta JSON (puedes personalizar esto según tus necesidades)
            return JsonResponse({'mensaje': 'Datos recibidos correctamente'})
        except Exception as e:
            return JsonResponse({'mensaje': f'Error interno del servidor: {str(e)}'}, status=500)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)



def visualization(request):
    datos = Sensor.objects.order_by('-updated_at')
    images = []

    for sensor in datos:
        # Configurar el tamaño del gráfico
        fig, ax = plt.subplots(figsize=(8, 6))

        # Obtener los datos para el sensor actual
        mediciones = sensor.mediciones.order_by('created_at')
        indices = list(range(1, len(mediciones) + 1))  # Numeración desde 1 hasta la cantidad de mediciones
        valores = [medicion.valor for medicion in mediciones]

        # Configurar el gráfico con colores y estilos personalizados
        ax.plot(indices, valores, marker='o', label=sensor.title, color='blue', linestyle='-', linewidth=2)
        
        # Configurar leyenda y etiquetas
        ax.legend()
        ax.set_xlabel('Número de medición')
        ax.set_ylabel('Valor de medición')

        # Agregar título con el nombre del sensor con estilo personalizado
        ax.set_title(sensor.title, fontsize=26, fontweight='bold', color='blue')


        # Convertir el gráfico en una imagen
        buffer = BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buffer)
        plt.close(fig)  # Cerrar la figura después de convertirla en una imagen

        # Codificar la imagen como base64 para mostrar en el HTML
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        images.append(image_data)

    return render(request, 'visualization/graphs.html', {
        'title': 'Gráficos',
        'images': images,
    })

def sensorList(request):
    sensores = Sensor.objects.order_by('created_at')

    return render(request, 'administration/list.html', {
        'title': 'Sensores',
        'sensores': sensores,
    })


def borrarSensor(request, id):
    sensor = Sensor.objects.get(pk=id)
    sensor.delete()

    return redirect('listado')
