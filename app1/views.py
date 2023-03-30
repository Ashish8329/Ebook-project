from django.shortcuts import render
from django.http import HttpResponse
from .models import Fe_b,cs_Decode,cs_SE,cs_TE,cs_BE

from .models import Aids_Decode,Aids_SE,Aids_TE,Aids_BE
from .models import It_Decode,It_SE,It_TE,It_BE
from .models import Etc_Decode,Etc_SE,Etc_TE,Etc_BE
from .models import civil_Decode,civil_SE,civil_TE,civil_BE
from .models import Mech_Decode,Mech_SE,Mech_TE,Mech_BE
from .models import Q_p


 
def Home(request):
    return render(request,'index.html')

def projects(request):
    return render(request,'projects.html')

def Q_paper(request):
    paper=Q_p.objects.all()
    return render(request,'Q.html',{'paper':paper})

def internship(request):
    return render(request,'internship.html')

# Create your views here.
def Fe_book(request):
    obj = Fe_b.objects.all()

    return render(request,'Fe_book.html',{'obj':obj})


def cs_book(request):
    deco =cs_Decode.objects.all() 
    second=cs_SE.objects.all()
    Third=cs_TE.objects.all()
    Fourth=cs_BE.objects.all()
    return render(request,'cs_books.html',{ 'second':second,'Third':Third,'Fourth':Fourth,'deco':deco})


def It_book(request):
    It_deco=It_Decode.objects.all()
    It_second=It_SE.objects.all()
    It_Third=It_TE.objects.all()
    It_Fourth=It_BE.objects.all()
    return render(request,'It_book.html',{'It_second':It_second,'It_Third':It_Third,'It_Fourth':It_Fourth,'It_deco':It_deco})


def Mech_book(request):
    M_deco=Mech_Decode.objects.all()
    M_second=Mech_SE.objects.all()
    M_Third=Mech_TE.objects.all()
    M_Fourth=Mech_BE.objects.all()
    return render(request,'M_book.html',{ 'M_second':M_second,'M_Third':M_Third,'M_Fourth':M_Fourth,'M_deco':M_deco})


 
def civil_book(request):
    civil_deco=civil_Decode.objects.all()
    civil_second=civil_SE.objects.all()
    civil_Third=civil_TE.objects.all()
    civil_Fourth=civil_BE.objects.all()
    return render(request,'civil_book.html',{ 'civil_second':civil_second,'civil_Third':civil_Third,'civil_Fourth':civil_Fourth,'civil_deco':civil_deco})


def Aids_book(request):
    Aids_deco=Aids_Decode.objects.all() 
    Aids_second=Aids_SE.objects.all()
    Aids_Third=Aids_TE.objects.all()
    Aids_Fourth=Aids_BE.objects.all()
    return render(request,'Aids_books.html',{'Aids_second':Aids_second,'Aids_Third':Aids_Third,'Aids_Fourth':Aids_Fourth,'Aids_deco':Aids_deco})

def Etc_book(request):
    Etc_deco=Etc_Decode.objects.all()
    Etc_second=Etc_SE.objects.all()
    Etc_Third=Etc_TE.objects.all()
    Etc_Fourth=Etc_BE.objects.all()
    return render(request,'Etc_book.html',{'Etc_second':Etc_second,'Etc_Third':Etc_Third,'Etc_Fourth':Etc_Fourth,'Etc_deco':Etc_deco})
