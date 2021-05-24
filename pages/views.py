from django.contrib.messages.api import success
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Client.models import Records, client
from web_project.forms import SaveClientRecord
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.conf import settings

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def Login_view_dentist(request, *args, **kwargs):
     return render(request, "Login.html", {})

def Contact_view(request, *args, **kwargs):
     return render(request, "Contact.html")

def home_view2():
    return render("home.html", {})

def check_user(name, contact_no):
     name = name
     contact_no = contact_no


def redirect_after_login(request):
    nxt = request.GET.get("next", None)
    if nxt is None:
        return redirect(settings.LOGIN_REDIRECT_URL)
    elif not is_safe_url(
            url=nxt,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return redirect(nxt)


def Login_view_client(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          contact_no = request.POST.get('contact_no')

          count = client.objects.all()
          lol =  client.objects.get(id = 1)
          
          for obj in count:
               x = (obj.name)
               y = (obj.contact_no)
               if(x==name and y==contact_no):
                    check_user(x,y)
                    print("success")
                    return redirect('Book_type')


     context = {
          
     }
     return render(request, "User_Login.html", context)

def Register_view(request):
     
     form = SaveClientRecord(request.POST)

     if request.method =='POST':
          print(request.method)
          if form.is_valid():
               form.save()
               return redirect('BK1_Login_client')

          

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

def BP1(request, *args, **kwargs):
     return render(request, "Booking-P1.html", {})