from django.contrib import admin
from .models import *
from import_export import resources

class EtudiantResource(resources.ModelResource):
    class Meta:
        model = Etudiant
        fields = '__all__'

admin.site.register(Etudiant)
admin.site.register(Domaine)
admin.site.register(Filiere)
admin.site.register(Verifier)

