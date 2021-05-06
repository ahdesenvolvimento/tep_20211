from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CadastroUser
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='login')
def index(request):
    users = Usuario.objects.all()
   # if request.user.is_anonymous:
    #    return redirect('login')
   # for i in users:
    #    i.delete()
    #for i in users:
       # i.delete()
    template_name = 'index'
    context = {
        'usuarios':users,
        'template':template_name
    }
    return render(request, 'index.html', context)


def login_page(request):
  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            print('Usuario não cadastrado')
            return redirect('login')
        else:
            print("existe")
            login(request, user)
            return redirect('index')
        
        
    return render(request, 'login.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form_user = CadastroUser(request.POST or None)
        if form_user.is_valid():
            form_user.save()
            return redirect('login')
    else:
        form_user = CadastroUser()
    
    context = {
        'form_user':form_user
    }
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')
    git = request.POST.get('github_user_ah')
    link = request.POST.get('linkedin_user_ah')
    port = request.POST.get('portfolio_user_ah')
    nome = request.POST.get('nome_user_ah')
    email = request.POST.get('email_user_ah')
    descricao = request.POST.get('descricao_user_ah')
    if username != None:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        usuario = Usuario.objects.create(
            nome_user_ah=nome,
            github_user_ah=git,
            linkedin_user_ah=link,
            portfolio_user_ah=port,
            descricao_user_ah=descricao,
            user=user  
        )
        usuario.save()
        return redirect('login')
    '''
        
    return render(request, 'cadastro_usuario.html', context)

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def perfil(request, pk):
    usuario = Usuario.objects.get(id=pk)
    print(usuario)
    form = CadastroUser(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'perfil.html', context)