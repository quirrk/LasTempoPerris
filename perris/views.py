from django.shortcuts import render
from .forms import PersonaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def persona_form(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('perris:index')
    else:
        form = PersonaForm()

    return render(request, 'voluntariado.html', {'form':form})