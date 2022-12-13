from django.db import models

import datetime

# Create your models here.
class Jedi(models.Model): 
    titulos_jedi = [
    ('Iniciado', 'Iniciado'),
    ('Padawan', 'Padawan'),
    ('Caballero', 'Caballero'),
    ('Maestro', 'Maestro'),
    ('Maestro de la Orden', 'Maestro de la Orden')
    ]
    colores = [
    ('Azul', 'Azul'),
    ('Verde', 'Verde'),
    ('Amarillo', 'Amarillo'),
    ('Violeta', 'Violeta'),
    ('Blanco', 'Blanco')
    ]

    nombre = models.CharField(max_length=100)
    numero_jedi = models.IntegerField()
    titulo = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=titulos_jedi,
        default=1
    )
    color_sable = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=colores,
        default=1
    )
    creado = models.DateField(
        auto_now_add=True,
    )

    #def __str__(self): #dundermethod: sirve para que cuando se ejecuta el print muestre los valores del return.
    #    return f"{self.nombre}, {self.numero_jedi}, {self.titulo}, {self.color_sable}, {self.id}"

class Sith(models.Model):
    titulos_sith = [
    ('Aprendíz', 'Aprendíz'),
    ('Lord', 'Lord'),
    ('Maestro', 'Maestro'),
    ]
    status = [
    ('Vivo', 'Vivo'),
    ('Muerto', 'Muerto'),
    ('Desconocido', 'Desconocido')
    ]

    nombre = models.CharField(max_length=100)
    numero_sith = models.IntegerField()
    titulo_sith = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices= titulos_sith,
        default=1
    )
    estado = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices= status,
        default=3
    )

class Androide(models.Model):
    tipo_utilidad = [
    ('Astromecánico', 'Astromecánico'),
    ('Asesino', 'Asesino'),
    ('Protocolo', 'Protocolo'),
    ('Otro', 'Otro')
    ]
    codigo = models.CharField(max_length=100)
    utilidad = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=tipo_utilidad,
        default=1
    )

