from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Client.models import client
from web_project.forms import SaveClientRecord
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def Login_view_dentist(request, *args, **kwargs):
     return render(request, "Login.html", {})

def Contact_view(request, *args, **kwargs):
     return render(request, "Contact.html", {})

def Login_view_client(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          contact_no = request.POST.get('contact_no')

          #count = client.objects.all().count()
          return  redirect('home')
     
     return render(request, "User_Login.html", {})

def Register_view(request):
     
     form = SaveClientRecord()

     if request.method =='POST':
          form  = SaveClientRecord(request.POST)
          if form.is_valid():
               form.save()
               print('Client is recorded in database')
               user = form.cleaned_data.get('name')
               messages.success(request, 'Account was created for ' + user)
               return redirect("BK1_Login_client")
          

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