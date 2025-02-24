from django.shortcuts import render, redirect
from .models import Proyecto, MensajeContacto, Habilidad,Certificacion,Testimonio,ImagenProyecto
from .forms import ContactForm, ProyectoForm, HabilidadForm,CertificacionForm,TestimonioForm
from django.shortcuts import render, get_object_or_404


def portfolio(request):
    proyectos = Proyecto.objects.all()
    habilidades = Habilidad.objects.all()
    certificaciones = Certificacion.objects.all()
    testimonios = Testimonio.objects.all()
    form = ContactForm()
    cert_form = CertificacionForm()
    testimonio_form = TestimonioForm()
    mensaje_exito = False
    mostrar_formulario = False

    if request.method == "POST":
        if "enviar_mensaje" in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                MensajeContacto.objects.create(
                    nombre=form.cleaned_data["nombre"],
                    email=form.cleaned_data["email"],
                    mensaje=form.cleaned_data["mensaje"]
                )
                form = ContactForm()
                mensaje_exito = True
        
        elif "agregar_certificacion" in request.POST:
            cert_form = CertificacionForm(request.POST)
            if cert_form.is_valid():
                cert_form.save()
                cert_form = CertificacionForm()

        elif "agregar_testimonio" in request.POST:
            testimonio_form = TestimonioForm(request.POST)
            if testimonio_form.is_valid():
                testimonio_form.save()
                testimonio_form = TestimonioForm()
                mensaje_exito = True
                mostrar_formulario = False  # Ocultar formulario después de enviarlo
        else:
            mostrar_formulario = True  # Mostrar formulario si no se ha enviado

    return render(
        request,
        "miapp/portfolio.html",
        {
            "proyectos": proyectos,
            "habilidades": habilidades,
            "certificaciones": certificaciones,
            "testimonios": testimonios,
            "form": form,
            "cert_form": cert_form,
            "testimonio_form": testimonio_form,
            "mensaje_exito": mensaje_exito,
            "mostrar_formulario": mostrar_formulario,
        }
    )


def proyecto_nuevo(request):
  if request.method == 'POST':
    form = ProyectoForm(
        request.POST,
        request.FILES)  # Incluye request.FILES para manejar archivos
    if form.is_valid():
      form.save()  # Guarda el objeto Proyecto
      return redirect(
          'portfolio'
      )  # Redirige a la lista de proyectos (ajusta el nombre de la URL)
  else:
    form = ProyectoForm()

  return render(request, 'miapp/proyecto_form.html', {'form': form})


def habilidad_nueva(request):
  if request.method == "POST":
    form = HabilidadForm(request.POST)
    if form.is_valid():
      habilidad = form.save()  # Guardamos la nueva habilidad
      return redirect('portfolio')  # Redirigir a la página del portfolio
  else:
    form = HabilidadForm()

  return render(request, 'miapp/habilidad_form.html', {'form': form})



def agregar_certificacion(request):
    if request.method == "POST":
        form = CertificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("portfolio")  # 🔹 Redirige a portfolio tras guardar
    else:
        form = CertificacionForm()

    return render(request, "miapp/agregar_certificacion.html", {"form": form})


def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, id=pk)
    imagenes = ImagenProyecto.objects.filter(proyecto=proyecto)
    print(f"Se encontraron {len(imagenes)} imágenes.")  # Verifica en el log
    return render(request, 'miapp/proyecto_detalle.html', {'proyecto': proyecto, 'imagenes': imagenes})
