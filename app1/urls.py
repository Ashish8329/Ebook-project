from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('projects/',views.projects,name='projects'),
    path('projects/',views.projects,name='projects'),
    path('FE_books',views.Fe_book,name='Fe_books'),
    path('cs_books/',views.cs_book,name='books'),
    path('It_books/',views.It_book,name='It_books'),
    path('Aids_books/',views.Aids_book,name='Aids_books'),
    path('civil_books/',views.civil_book,name='civil_books'),
    path('Etc_books/',views.Etc_book,name='Etc_books'),
    path('Mech_books/',views.Mech_book,name='Mech_books'),
    path('Qeutions_paper/',views.Q_paper,name='Qeutions_paper'),
    path('internship/',views.internship,name='internship'),

    
]
