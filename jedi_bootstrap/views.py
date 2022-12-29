from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from jedi_bootstrap.models import Post, Avatar, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.admin import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UsuarioForm, Buscar


def index(request):
    posts = Post.objects.order_by("-publicado_el").all()
    return render(request, 'jedi_bootstrap/index.html', {"posts":posts})

def about(request):
    return render(request, 'jedi_bootstrap/about.html')

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('jedi-posteos')
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('jedi-posteos')

class PostActualizar(LoginRequiredMixin, UpdateView):
    template_name = 'jedi_bootstrap/post_update.html'
    model = Post
    success_url = reverse_lazy("jedi-posteos")
    fields = ['titulo','sub_titulo', 'texto']
    
class PostDetalle(DetailView):
    model = Post

#User management

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('jedi-index')

class UserLogin(LoginView):
    next_page = reverse_lazy('jedi-index')

class UserLogout(LogoutView):
    next_page = reverse_lazy('jedi-index')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name','last_name', 'email']
    success_url = reverse_lazy('jedi-index')

#AVATAR
class AvatarCrear(LoginRequiredMixin, CreateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('jedi-index')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('jedi-index')

#Mensajeria
class MensajeCrear(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-lista')
    fields = ['nombre','email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-lista')
   
class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeList(ListView):
    model = Mensaje

class MensajeRespuesta(UpdateView):
    model = Mensaje
    fields = ['respuesta']
    success_url = reverse_lazy('mensaje-lista')


