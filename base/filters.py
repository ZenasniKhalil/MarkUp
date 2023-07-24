import django_filters
from .models import Etudiant, Verifier, Domaine, Filiere, niveaux

def domaine_choices():
    domaines = Domaine.objects.all()
    domaine_list = []
    for domaine in domaines:
        domaine_list.append((domaine.code, domaine.nom))
    return domaine_list

def filiere_choices():
    filieres = Filiere.objects.all()
    filiere_list = []
    for filiere in filieres:
        filiere_list.append((filiere.code,filiere.nom))
    return filiere_list


class EtudiantFilter(django_filters.FilterSet):
    mat = django_filters.CharFilter(field_name='mat',lookup_expr='icontains')
    nom = django_filters.CharFilter(field_name='nom',lookup_expr='icontains')
    prenom = django_filters.CharFilter(field_name='prenom',lookup_expr='icontains')
    year = django_filters.NumberFilter(field_name='date_de_naissance',lookup_expr='year')
    month = django_filters.NumberFilter(field_name='date_de_naissance',lookup_expr='month')
    day = django_filters.NumberFilter(field_name='date_de_naissance',lookup_expr='day')
    class Meta:
        model = Etudiant
        fields = '__all__'

class VerifierFilter(django_filters.FilterSet):
    mat = django_filters.CharFilter(field_name='etudiant__mat',lookup_expr='icontains')
    nom = django_filters.CharFilter(field_name='etudiant__nom',lookup_expr='icontains')
    prenom = django_filters.CharFilter(field_name='etudiant__prenom',lookup_expr='icontains')
    domaine = django_filters.ChoiceFilter(field_name='etudiant__domaine',choices=domaine_choices)
    filiere = django_filters.ChoiceFilter(field_name='etudiant__filiere',choices=filiere_choices) 
    niveau = django_filters.ChoiceFilter(field_name='etudiant__niveau',choices=niveaux)
    year = django_filters.NumberFilter(field_name='etudiant__date_de_naissance',lookup_expr='year')
    month = django_filters.NumberFilter(field_name='etudiant__date_de_naissance',lookup_expr='month')
    day = django_filters.NumberFilter(field_name='etudiant__date_de_naissance',lookup_expr='day')
    date = django_filters.DateFilter(field_name='date')
    time_gt = django_filters.TimeFilter(field_name='temp',lookup_expr='gt')
    time_lt = django_filters.TimeFilter(field_name='temp',lookup_expr='lt')
    class Meta:
        model = Verifier
        fields = '__all__'