from django.contrib import admin
from .models import Proyecto, Habilidad, MensajeContacto, Certificacion, Testimonio

admin.site.register(MensajeContacto)
admin.site.register(Proyecto)
admin.site.register(Certificacion)  # Se agrega Certificacion
admin.site.register(Testimonio)  # Se agrega Testimonio al admin

# Si deseas personalizar la vista en el admin para Habilidad
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel')  # Muestra los campos deseados
    search_fields = ('nombre',)  # Permite búsqueda por nombre

admin.site.register(Habilidad, HabilidadAdmin)
