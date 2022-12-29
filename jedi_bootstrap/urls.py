from django.urls import path, include
from .views import (index, about, PostList, PostCrear, PostBorrar, 
                    PostDetalle, PostActualizar, UserSignUp,
                    UserLogin, UserLogout, AvatarCrear, AvatarActualizar,
                    UserActualizar, MensajeCrear, MensajeBorrar,
                    MensajeDetalle, MensajeList, MensajeRespuesta,
                    )
from django.contrib.admin.views.decorators import staff_member_required #permite bloquear solo para el superuser
urlpatterns = [
    path('jedi-blog/', index, name='jedi-index'),
    path('jedi-blog/about', about, name='about'),
    path('jedi-blog/listar/', PostList.as_view(), name='jedi-posteos'),
    path('jedi-blog/listar/nuevo-post/', PostCrear.as_view(), name='jedi-newpost'),
    path('jedi-blog/<int:pk>/borrar/', PostBorrar.as_view(), name='post-borrar'),
    path('jedi-blog/listar/<int:pk>/post-detail/', PostDetalle.as_view(), name = 'post-detalle'),
    path('jedi-blog/listar/<int:pk>/post-update/', PostActualizar.as_view(), name = 'post-actualizar'),
    path('jedi-blog/signup/', UserSignUp.as_view(), name='jedi-signup'),
    path('jedi-blog/login/', UserLogin.as_view(), name='jedi-login'),
    path('jedi-blog/logout/', UserLogout.as_view(), name='jedi-logout'),
    path('jedi-blog/avatars/crear/', AvatarCrear.as_view(), name = 'crear-avatar'),
    path('jedi-blog/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name = 'jedi-avatar'),
    path('jedi-blog/users/<int:pk>/actualizar/', UserActualizar.as_view(), name= 'user-actualizar'),
    path('jedi-blog/mensajes/', MensajeList.as_view(), name='mensaje-lista'),
    path('jedi-blog/mensajes/nuevo-mensaje/', MensajeCrear.as_view(), name='mensaje-nuevo'),
    path('jedi-blog/mensajes/<int:pk>/borrar/', staff_member_required(MensajeBorrar.as_view()), name='mensaje-borrar'),
    path('jedi-blog/listar/<int:pk>/mensaje-detail/', MensajeDetalle.as_view(), name = 'mensaje-detalle'),
    path('jedi-blog/listar/<int:pk>/mensaje-response/', staff_member_required(MensajeRespuesta.as_view()), name = 'mensaje-responder'),
]