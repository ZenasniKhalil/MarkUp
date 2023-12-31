from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class CreateUser(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Entrez votre mot de passe'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirmez votre mot de passe'})
    )
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'nom d\'utilisateur'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prenom'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }