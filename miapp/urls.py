from django.urls import path
from .views import portfolio, habilidad_nueva,agregar_certificacion,proyecto_detalle
from . import views  # Aquí importamos views

urlpatterns = [
    path('', portfolio, name='portfolio'),  # Página principal
    path('portfolio', portfolio, name='portfolio'),  # Página principal
    path('proyecto_nuevo', views.proyecto_nuevo, name='proyecto_nuevo'),
    path('habilidad_nueva/', habilidad_nueva, name='habilidad_nueva'),
    path("agregar_certificacion/", agregar_certificacion, name="agregar_certificacion"),
    path('proyectos/<int:pk>/', proyecto_detalle, name='proyecto_detalle'),


]
