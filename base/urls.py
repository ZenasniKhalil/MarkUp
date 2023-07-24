from django.urls import path
from . import views
app_name='base'
urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('ajouter-etudiants/', views.addStudent, name='add_student'),
    path('etudiants/', views.student, name='student'),
    path('sup-etudiants/', views.deleteStudents, name='sup_etudiants'),
    path('ajouter-domaine/',views.addDomaine, name='ajouter-domaine'),
    path('ajouter-filiere/',views.addFiliere, name='ajouter-filiere'),
    path('export/',views.downloadRepport, name='export'),
]
