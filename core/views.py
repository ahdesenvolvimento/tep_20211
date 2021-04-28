from django.shortcuts import render

# Create your views here.

def index(request):
    texto = '<h1>Ola</h1>'
    context = {
        'texto':texto
    }
    return render(request, 'index.html', context)
