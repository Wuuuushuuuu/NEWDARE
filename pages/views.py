from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Client.models import Records, client
from web_project.forms import SaveClientRecord
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def Login_view_dentist(request, *args, **kwargs):
     return render(request, "Login.html", {})

def Contact_view(request, *args, **kwargs):
     return redirect('https://www.youtube.com/watch?v=ekyCxgtW3Js&ab_channel=DennisIvyDennisIvyVerified')

def Login_view_client(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          contact_no = request.POST.get('contact_no')

          #count = client.objects.all().count()
          return  redirect('app:home')
     
     return render(request, "User_Login.html", {})

def Register_view(request):
     
     form = SaveClientRecord()

     if request.method =='POST':
         name = request.POST['name']
         email = request.POST['email']
         contact_no = request.POST['contact_no']
         client = Records(Name=name,Email=email,Contact_no = contact_no)
         client.save()
         return redirect('home')
     else:
          return render(request, "Register.html")
          

     context = {'form': form} 
     return render(request, "Register.html", context)

def Dentist_Acct_View(request, *args, **kwargs):
     return render(request, "Account.html", {})

def Dentist_Apnt_View(request, *args, **kwargs):
     return render(request, "Appointments.html", {})

def Dentist_Dashboard(request, *args, **kwargs):
     return render(request, "Main-Dashboard.html", {})

def Dentist_Records(request, *args, **kwargs):
     return render(request, "Records.html", {})