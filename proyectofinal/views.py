from django.shortcuts import render, get_object_or_404
from django.views import View
from proyectofinal.models import Jedi
from proyectofinal.forms import Buscar, JediForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

#Create your views here.
def pasar_path(request, id):
    return id

def home(request):
    return render(request, "proyectofinal/home.html")

def mostrarjedis(request):
    lista_jedis = Jedi.objects.all()
    return render(request, 'proyectofinal/jedis.html', {'lista_jedis': lista_jedis})

class ListaJedis(ListView):
    model = Jedi

class DetalleJedi(DetailView):
    model = Jedi

class NuevoJedi(CreateView):
    model = Jedi
    success_url = reverse_lazy("jedis-panel")
    fields = ['nombre','numero_jedi', 'titulo', 'color_sable']

class BorrarJedi(DeleteView):
    model = Jedi
    success_url = reverse_lazy("jedis-panel")

class JediActualizar(UpdateView):
    template_name = 'proyectofinal/jedi_update.html'
    model = Jedi
    success_url = reverse_lazy("jedis-panel")
    fields = ['nombre','numero_jedi', 'titulo', 'color_sable']

class BuscarJedi(View):
    form_class = Buscar
    template_name = 'proyectofinal/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_jedis = Jedi.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_jedis':lista_jedis})
        return render(request, self.template_name, {"form": form})

""" class AltaJedi(View):
    form_class = JediForm
    template_name = 'proyectofinal/alta_jedi.html'
    initial = {'nombre':'','numero_jedi':'', 'titulo':'', 'color_sable':''}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se carg?? con ??xito al nuevo integrante del Sindicato Jedi, {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito':msg_exito})
        return render(request, self.template_name, {"form": form}) """

"""class ActualizarJedi(View):
  form_class = JediForm
  template_name = 'proyectofinal/actualizar_jedi.html'
  initial = {'nombre':'','numero_jedi':'', 'titulo':'', 'color_sable':''}

  # prestar atenci??n ahora el method get recibe un parametro pk == primaryKey == identificador ??nico
  def get(self, request, pk): 
      jedi = get_object_or_404(Jedi, pk=pk)
      form = self.form_class(instance=jedi)
      return render(request, self.template_name, {'form':form,'jedi': jedi})

  # prestar atenci??n ahora el method post recibe un parametro pk == primaryKey == identificador ??nico
  def post(self, request, pk): 
      jedi = get_object_or_404(Jedi, pk=pk)
      form = self.form_class(request.POST ,instance=jedi)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualiz?? con ??xito el integrante {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'jedi': jedi,
                                                      'msg_exito': msg_exito})

      return render(request, self.template_name, {"form": form})"""

"""class BorrarJedi(View):
  template_name = 'proyectofinal/jedis.html'

  def get(self, request, pk): 
      jedi = get_object_or_404(Jedi, pk=pk)
      jedi.delete()
      lista_jedis = Jedi.objects.all()
      return render(request, self.template_name, {'lista_jedis': lista_jedis})"""

