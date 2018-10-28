from django.shortcuts import render
from .forms import PersonaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def voluntario(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
    form = PersonaForm()
    return render(request, 'voluntariado.html', {'form': form})


def mascotas(request):
    return render(request, 'mascotas.html')