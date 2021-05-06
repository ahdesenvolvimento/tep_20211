from django import forms
from blog.models import Postagem
class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
        exclude = ['slug_postagem_ah']