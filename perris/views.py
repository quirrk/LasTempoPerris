from django.shortcuts import render
from .forms import PersonaForm
from django.contrib.auth.decorators import login_required
from .models import Perro
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
    

@login_required
def voluntario(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            Persona = form.save(commit=False)
            Persona.save()
            return redirect('mascotas')
    else:
        form = PersonaForm()
    return render(request, 'voluntariado.html', {'form': form})


def mascotas(request):
    perrisD=Perro.objects.filter(estado__contains='DI')
    perrisA=Perro.objects.filter(estado__contains='AD')
    perrisR=Perro.objects.filter(estado__contains='RE')
    return render(request, 'mascotas.html',{'perrisD':perrisD,'perrisA':perrisA,'perrisR':perrisR})



