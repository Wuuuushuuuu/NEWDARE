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