from django.urls import path
from .views import home, mostrarjedis, BuscarJedi, AltaJedi, ActualizarJedi, BorrarJedi

urlpatterns = [
    path('home/', home, name='home'),
    path('jedis/', mostrarjedis, name='jedis-integrantes'),
    path('jedis/buscar/', BuscarJedi.as_view(), name='jedis-buscar'),
    path('jedis/alta/', AltaJedi.as_view(), name='jedis-alta'),
    path('jedis/actualizar/<int:pk>', ActualizarJedi.as_view(), name='jedis-actualizar'),
    path('jedis/borrar/<int:pk>', BorrarJedi.as_view(), name='jedis-borrar')
]