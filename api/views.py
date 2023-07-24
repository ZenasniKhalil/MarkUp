from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VerifierSerializer, EtudiantSerializer
from base.models import Verifier ,Etudiant

@api_view(['GET'])
def getStudent(request,mat):
    student = Etudiant.objects.get(mat=mat)
    serializer = EtudiantSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createRecord(request):
    serializer = VerifierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
