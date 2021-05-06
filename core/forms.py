from django import forms
from .models import Usuario


class CadastroUser(forms.ModelForm):
 
    class Meta:
        model = Usuario
        fields = [
            'nome_user_ah', 
            'email_user_ah', 
            'github_user_ah', 
            'linkedin_user_ah', 
            'portfolio_user_ah',
            'descricao_user_ah',
            'username', 
            'password'
        ]
    
    def save(self, commit=True):
        user = super(CadastroUser, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
    def clean(self):
        print(self.cleaned_data)
