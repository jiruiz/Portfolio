from django.db import models


class Proyecto(models.Model):
  nombre = models.CharField(max_length=200)
  descripcion = models.TextField()
  tecnologias = models.CharField(max_length=200)
  imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)
  enlace = models.URLField(max_length=200, null=True,
                           blank=True)  # Agrega el campo enlace

  def __str__(self):
    return self.nombre


class MensajeContacto(models.Model):
  nombre = models.CharField(max_length=100)
  email = models.EmailField()
  mensaje = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.nombre} - {self.email}"


class Habilidad(models.Model):
  nombre = models.CharField(max_length=200)
  nivel = models.IntegerField(choices=[(i, f"{i}%")
  for i in range(0, 101, 10)],
  default=0)

  def __str__(self):
    return self.nombre



class Certificacion(models.Model):
    nombre = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.plataforma}"


class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonio de {self.nombre} ({self.empresa})"        