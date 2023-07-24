from django.shortcuts import render,redirect
from .importExportExcel import importExcel, exportExcel
from .models import Etudiant,Verifier, Domaine, Filiere
from django.contrib import messages
from .forms import DomaineForm, FiliereForm
from .filters import EtudiantFilter, VerifierFilter
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import csv

@login_required(login_url='/login/')
def dashboard(request):
    table_header = ['Mat. Etudiant',
                    'Nom',
                    'Prénom',
                    'Date de naiss.',
                    'Code domaine',
                    'Code filière',
                    'Code niveau',
                    'Date de l\'examen',
                    'Heure de l\'examen']
    records = VerifierFilter(request.GET, queryset=Verifier.objects.all())
    request.session['recods'] = request.GET
    context={
        'records':records,
        'header':table_header,
        'admin': request.user.groups.filter(name='admins').exists(),
        'stuff':request.user.groups.filter(name='stuff').exists(),
    }
    return render(request, 'base/records.html', context)

@login_required(login_url='/login/')
def student(request):
    table_header = ['Mat. Etudiant',
                    'Nom',
                    'Prénom',
                    'Date de naiss.',
                    'Code domaine',
                    'Code filière',
                    'Code niveau']
    students = EtudiantFilter(request.GET, queryset=Etudiant.objects.all())
    context = {
        'students':students,
        'header':table_header,
        'admin': request.user.groups.filter(name='admins').exists(),
        'stuff':request.user.groups.filter(name='stuff').exists(),
    }
    return render(request, 'base/student.html',context)

@login_required(login_url='/login/')
@permission_required('base.add_etudiant')
def addStudent(request):
    if request.method == 'POST':
        if request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            redir = importExcel(request,myfile)
            if(redir):
                return redirect('base:student')
        else:
            messages.error(request, 'Vous n\'avez pas selction un fichier excel !!! ')
    return render(request, 'base/ajouter-etudiants.html')

@login_required(login_url='/login/')
@permission_required('base.delete_etudiant')
def deleteStudents(request):
    if request.method == 'POST':
        Etudiant.objects.all().delete()
        return redirect('base:student')
    return render(request, 'base/sup_etudiants.html')

@login_required(login_url='/login/')
@permission_required('base.add_domaine')
def addDomaine(request):
    form = DomaineForm()
    if request.method == 'POST':
        try:
            Domaine.objects.create(
                code=request.POST.get('code'),
                nom=request.POST.get('nom')
            )
            return redirect('base:dashboard')
        except IntegrityError as e:
            messages.error(request, 'Le Code <strong>'+str(request.POST.get('code'))+'</strong> est deja existant !!!')
        
    context={
        'form':form
    }
    return render(request, 'base/domaine.html',context)

@login_required(login_url='/login/')
@permission_required('base.add_filiere')
def addFiliere(request):
    form = FiliereForm()
    if request.method == 'POST':
        try:
            Filiere.objects.create(
                code=request.POST.get('code'),
                nom=request.POST.get('nom')
            )
            return redirect('base:dashboard')
        except IntegrityError as e:
            messages.error(request, 'Le Code <strong>'+str(request.POST.get('code'))+'</strong> est deja existant !!!')
        
    context={
        'form':form
    }
    return render(request, 'base/filiere.html',context)

def downloadRepport(request):
    records = VerifierFilter(request.session['recods'], queryset=Verifier.objects.all())
    print(records)
    #records = Verifier.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] =  'attachement; filename=list_etudiant.xlsx'
    writer = csv.writer(response)
    writer.writerow(['Mat. Etudiant',
                     'Nom',
                     'Prénom',
                     'Date de naiss.',
                     'Code domaine',
                     'Code filière',
                     'Code niveau',
                     "Date de l'examen",
                     "Heure de l'examen"],)
    
    print('hello')
    for record in records.qs:
        writer.writerow([record.etudiant.mat,
                         record.etudiant.nom,
                         record.etudiant.prenom,
                         record.etudiant.date_de_naissance,
                         record.etudiant.domaine,
                         record.etudiant.filiere,
                         record.etudiant.niveau,
                         record.date,
                         record.temp])
    return response




