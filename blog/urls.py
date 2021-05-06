from django.urls import path
from blog.views import *
urlpatterns = [
     path('', blog, name='blog'),
     path('criar/postagem', criar_postagem, name='criar_postagem'),
     path('visualizar/postagem/<str:slug>', visualizar_postagem, name='visualizar_postagem'),
]