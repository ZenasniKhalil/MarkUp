from django.urls import path
from . import views
urlpatterns = [
    path('get-student/<str:mat>/',views.getStudent, name='get-student'),
    path('create-record/',views.createRecord, name='create-record'),
]