from django.contrib import admin
from .models import Proyecto, Habilidad, MensajeContacto, Certificacion, Testimonio, ImagenProyecto

# Configuración inline para mostrar imágenes dentro de Proyecto
class ImagenProyectoInline(admin.TabularInline):  # También puedes usar StackedInline
    model = ImagenProyecto
    extra = 3  # Número de imágenes adicionales vacías que se pueden agregar

# Personalización del admin de Proyecto
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tecnologias')  # Campos visibles en la lista de proyectos
    search_fields = ('nombre', 'tecnologias')  # Búsqueda por nombre y tecnologías
    inlines = [ImagenProyectoInline]  # Muestra imágenes asociadas al proyecto

# Registro de modelos en el admin
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(ImagenProyecto)  # Se registra también para acceso independiente
admin.site.register(MensajeContacto)
admin.site.register(Certificacion)
admin.site.register(Testimonio)

# Personalización del admin para Habilidad
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel')
    search_fields = ('nombre',)

admin.site.register(Habilidad, HabilidadAdmin)
