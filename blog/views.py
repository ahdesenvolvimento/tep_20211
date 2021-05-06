from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.forms import *
from blog.models import *

def blog(request):
    postagens = Postagem.objects.all()
    context = {
        'postagens':postagens
    }
    return render(request, 'blog.html', context)

@login_required(login_url='login')
def criar_postagem(request):
    if request.method == 'POST':
        form_post = PostagemForm(request.POST or None)
        if form_post.is_valid():
            form_post.save()
            return redirect('blog')
        
    else:
        form_post = PostagemForm()
    context = {
        'form':form_post
    }
    return render(request, 'criar_postagem.html', context)

def visualizar_postagem(request, slug):
    postagem = Postagem.objects.get(slug_postagem_ah=slug)
    context = {
        'postagem':postagem
    }
    return render(request, 'visualizar_postagem.html', context)
# Create your views here.
