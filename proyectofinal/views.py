from django.shortcuts import render, get_object_or_404
from django.views import View
from proyectofinal.models import Jedi
from proyectofinal.forms import Buscar, JediForm

# Create your views here.
def home(request):
    return render(request, "proyectofinal/home.html")

def mostrarjedis(request):
    lista_jedis = Jedi.objects.all()
    return render(request, 'proyectofinal/jedis.html', {'lista_jedis': lista_jedis})

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

class AltaJedi(View):
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
            msg_exito = f"Se cargó con éxito al nuevo integrante del Sindicato Jedi, {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito':msg_exito})
        return render(request, self.template_name, {"form": form})

class ActualizarJedi(View):
  form_class = JediForm
  template_name = 'proyectofinal/actualizar_jedi.html'
  initial = {'nombre':'','numero_jedi':'', 'titulo':'', 'color_sable':''}

  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      jedi = get_object_or_404(Jedi, pk=pk)
      form = self.form_class(instance=jedi)
      return render(request, self.template_name, {'form':form,'jedi': jedi})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      jedi = get_object_or_404(Jedi, pk=pk)
      form = self.form_class(request.POST ,instance=jedi)
      if form.is_valid():
          form.save()
          msg_exito = f"Se actualizó con éxito el integrante {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'jedi': jedi,
                                                      'msg_exito': msg_exito})

      return render(request, self.template_name, {"form": form})

class BorrarJedi(View):
  template_name = 'proyectofinal/jedis.html'

  def get(self, request, pk): 
      jedi = get_object_or_404(Jedi, pk=pk)
      jedi.delete()
      lista_jedis = Jedi.objects.all()
      return render(request, self.template_name, {'lista_jedis': lista_jedis})