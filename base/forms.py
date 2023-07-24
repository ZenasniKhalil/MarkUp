from .models import Etudiant, Domaine, Filiere
from django.forms import ModelForm
from django import forms

class DomaineForm(ModelForm):
    class Meta:
        model = Domaine
        fields = '__all__'

class FiliereForm(ModelForm):
    class Meta:
        model = Filiere
        fields = '__all__'