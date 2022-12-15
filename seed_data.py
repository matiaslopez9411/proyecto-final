from proyectofinal.models import Jedi
from random import randint, choice
from nombres import nombres_random

titulos_jedi = ['Iniciado', 'Padawan', 'Caballero', 'Maestro']
colores = ['Azul', 'Verde', 'Amarillo', 'Violeta', 'Violeta', 'Blanco']

for x in range(10):
    Jedi(nombre= choice(nombres_random), numero_jedi=randint(100000,999999), titulo=str(choice(titulos_jedi)), color_sable=str(choice(colores))).save()

print("Se cargaron con éxito los usuarios de pruebas")