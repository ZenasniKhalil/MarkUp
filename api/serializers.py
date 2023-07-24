from rest_framework import serializers
from base.models import Verifier , Etudiant


class VerifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verifier
        fields = '__all__'

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'