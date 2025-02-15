from django import forms
from .models import Proyecto, MensajeContacto, Habilidad,Certificacion, Testimonio


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={"class": "input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input"}))
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={"class": "textarea"}))


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'tecnologias', 'imagen',
                  'enlace']  # Agrega 'enlace' aquí

    enlace = forms.URLField(
        max_length=200,
        required=False,
        widget=forms.URLInput(
            attrs={'placeholder': 'Ingresa un enlace (opcional)'}))


class HabilidadForm(forms.ModelForm):

    class Meta:
        model = Habilidad
        fields = ['nombre',
                  'nivel']  # Los campos que quieras incluir en el formulario


class CertificacionForm(forms.ModelForm):
    class Meta:
        model = Certificacion
        fields = ["nombre", "plataforma"]


class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['nombre', 'empresa', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }   
