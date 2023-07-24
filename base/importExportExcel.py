from .models import Etudiant, Domaine, Filiere
import pandas as pd
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponse
import csv

def importExcel(request,myfile):       
    dbframe = pd.read_excel(myfile)
    if list(dbframe.columns) == ['Mat. Etudiant',
                                 'Nom',
                                 'Prénom',
                                 'Date de naiss.',
                                 'Code domaine',
                                 'Code filière',
                                 'Code niveau']:
        student_number = 0;
        for dbframe in dbframe.itertuples():
            domaine_instance = Domaine.objects.get(code=dbframe[5])
            filiere_instance = Filiere.objects.get(code=dbframe[6])
            reformating_date = datetime.strptime(dbframe[4], '%d/%m/%Y').date()
            try:
                obj = Etudiant.objects.create(
                    mat=dbframe[1],
                    nom=dbframe[2],
                    prenom=dbframe[3],
                    date_de_naissance=reformating_date,
                    domaine=domaine_instance,
                    filiere=filiere_instance,
                    niveau=dbframe[7]
                )           
                obj.save()
                student_number+=1;
            except IntegrityError as e:
                pass
            # exception for missing value
        messages.success(request, str(student_number)+' étudiants sont ajoutés ')
        # this variable for redirection in views page
        redir = True
    else:
        # this variable for redirection in views page
        redir = False; 
        messages.error(request, 'le tableau que vous insérez ne respecte pas les noms des colonnes suivantes: <br> <strong>Mat. Etudiant, Nom, Prénom, Date de naiss. , Code domaine , Code filière , Code niveau</strong> ')
    return redir


def exportExcel():
    students = Etudiant.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Dispostion'] =  'attachement; filename=list_etudiant.csv'
    writer = csv.writer(response)
    writer.writerow(['Mat. Etudiant',
                     'Nom',
                     'Prénom',
                     'Date de naiss.',
                     'Code domaine',
                     'Code filière',
                     'Code niveau'])
    for student in list(students.values()):
        writer.writerow(student)
    return response