from django.db import models
from django.contrib.auth.admin import User


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateField(
        auto_now_add=True,
    )
    imagen = models.ImageField(upload_to="posteos", null="True", blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", null="True", blank=True)

class Mensaje(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    enviado_el = models.DateField(
        auto_now_add=True
    )
    respuesta = models.TextField(
        max_length=3000,
        null="True", blank=True,
        default="En breve alguno de nuestros integrantes brindará una respuesta"
        )