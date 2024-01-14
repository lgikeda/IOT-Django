from django.urls import path
from . import views

urlpatterns = [
    path('crear_control/', views.crear_control, name='crear_control'),
    path('controls/', views.mostrar_controles, name='controls'),
    path('cambiar_estado/<int:control_id>/', views.cambiar_estado, name='cambiar_estado'),
    path('borrarControl/<int:id>', views.borrarControl, name='borrarControl'),
]
