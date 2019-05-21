from django.shortcuts import render
from .forms import PersonaForm
from django.contrib.auth.decorators import login_required
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
            return redirect('index.html')
    else:
        form = PersonaForm()
    return render(request, 'voluntariado.html', {'form': form})



