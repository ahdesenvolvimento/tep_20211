from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('cadastrar/usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('perfil/<int:pk>', perfil, name='perfil'),
]