from django.db import models
from core.models import Usuario
from django.db.models import signals
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField 
# Create your models here.

class Criacao(models.Model):
    criacao = models.DateField(auto_now_add=True)
    horario = models.TimeField(auto_now_add=True)
    
class Postagem(Criacao):
    codigo_postagem_ah = models.AutoField(primary_key=True)
    titulo_postagem_ah = models.CharField(max_length=120, blank=False, null=True)
    corpo_postagem_ah = RichTextField(max_length=15000, null=True, blank=True)
    autor_postagem_ah = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug_postagem_ah = models.SlugField(max_length=240, blank=True, null=True)
    
def postagem_pre_save(signal, instance, sender, **kwargs):
    instance.slug_postagem_ah = slugify(instance.titulo_postagem_ah)
signals.pre_save.connect(postagem_pre_save, sender=Postagem)
    
        
