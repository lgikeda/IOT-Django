from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name="index"),
    path('visualization/', views.visualization, name="visualization"),
    path('recibirDatos/', views.recibirDatos, name='recibir'),
    path('borrarSensor/<int:id>', views.borrarSensor, name='borrar'),
    path('list/', views.sensorList, name='listado'),
]
