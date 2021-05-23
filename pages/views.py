from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def Login_view_dentist(request, *args, **kwargs):
     return render(request, "Login.html", {})

def Contact_view(request, *args, **kwargs):
     return render(request, "Contact.html", {})

def Login_view_client(request, *args, **kwargs):
     return render(request, "User_Login.html", {})

def Register_view(request, *args, **kwargs):
     



     return render(request, "Register.html", {})

def Dentist_Acct_View(request, *args, **kwargs):
     return render(request, "Account.html", {})

def Dentist_Apnt_View(request, *args, **kwargs):
     return render(request, "Appointments.html", {})

def Dentist_Dashboard(request, *args, **kwargs):
     return render(request, "Main-Dashboard.html", {})

def Dentist_Records(request, *args, **kwargs):
     return render(request, "Records.html", {})