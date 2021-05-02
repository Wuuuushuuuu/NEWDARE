from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def Login_view(request, *args, **kwargs):
     return render(request, "Login.html", {})

def Contact_view(request, *args, **kwargs):
     return render(request, "Contact.html", {})