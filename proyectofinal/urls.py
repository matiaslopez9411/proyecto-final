from django.urls import path
from .views import home, ListaJedis, BuscarJedi, NuevoJedi, JediActualizar, BorrarJedi, DetalleJedi 

urlpatterns = [
    path('home/', home, name='home'),
    path('panel-jedis/', ListaJedis.as_view(), name='jedis-panel'),
    path('jedis/buscar/', BuscarJedi.as_view(), name='jedis-buscar'),
    path('panel-jedis/alta-jedi/', NuevoJedi.as_view(), name='jedis-alta'),
    path('panel-jedis/<int:pk>/actualizar/', JediActualizar.as_view(), name='jedis-actualizar'),
    path('panel-jedis/<int:pk>/borrar/', BorrarJedi.as_view(), name='jedis-borrar'),
    path('panel-jedis/<int:pk>/detalle/', DetalleJedi.as_view(), name='jedis-detalle')
]