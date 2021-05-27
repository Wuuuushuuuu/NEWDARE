from django.contrib.messages.api import success
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Dentist_Acct.models import Dentist_Acct
from Client.models import Records, client, Bookings, Logged_in
from web_project.forms import SaveClientRecord, ContactForm, UpdateForm
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from datetime import datetime as dt
import datetime


# Create your views here

def home_view(request, *args, **kwargs):

    return render(request, "home.html", {})

def Login_view_dentist(request, *args, **kwargs):
     if request.method == 'POST':
          name = request.POST.get('name')
          password = request.POST.get('Password')

          count = Dentist_Acct.objects.all()

          for obj in count:
               x = (obj.Username)
               y = (obj.Password)
               if(x==name and y==password):
                    print("success")
                    return redirect('DentistDB')

     return render(request, "Login.html", {})

def Contact_view(request, *args, **kwargs):
     return render(request, "Contact.html",  {})



def home_view2():
    return render("home.html", {})

def check_user(name, contact_no):
     Name = name
     Contact_no = contact_no
     list =[]
     list.append(Name)
     list.append(Contact_no)
     return list


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
                    Logs =  Logged_in(Name = x, Contact_no = y)
                    Logs.save()
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
     Account = Dentist_Acct.objects.get(id=1)
     print(Account.Name)
     return render(request, "Account.html", {'Account': Account})

def Dentist_Apnt_View(request, *args, **kwargs):
     books = Bookings.objects.all()
     return render(request, "Appointments-2.html", {'books':books})

def Dentist_Dashboard(request, *args, **kwargs):
     Pending = Bookings.objects.filter(Status = "Pending").count()
     Confimred = Bookings.objects.filter(Status = "CONFIRMED").count()
     date_today = (datetime.date.today())
     Date = Bookings.objects.filter(Date = date_today).count()

     context = {
          'Pending':Pending,
          'Confirmed':Confimred,
          'Date':Date
     }
     return render(request, "Dentist-Dashboard.html", context)

def Dentist_Records(request, *args, **kwargs):
     return render(request, "Records.html", {})

def BP1(request, *args, **kwargs):
     if request.method == 'POST':
          date = request.POST['date']
          concerns = request.POST['select']
          time = request.POST['radiobutton']
          logs =  Logged_in.objects.all()
          for obj in  Logged_in.objects.all():
               x = obj.Name
               y = obj.Contact_no
          record =  Bookings(Name = x, Contact_no = y, Date = date, Concern = concerns, time = time)
          record.save()
          logs.delete()
          return redirect('home')

     return render(request, "Booking-P2.html", {})

def About(request, *args, **kwargs):
     return render(request, "About.html", {})

def Service(request, *args, **kwargs):
     return render(request, "Services.html", {})


def updateAppointment(request, pk):
     order = Bookings.objects.get(id =pk)
     form  = UpdateForm(instance = order)

     if request.method == 'POST':
          form = UpdateForm(request.POST, instance=order)
          if form.is_valid():
               form.save()
               return redirect('DentistDB')
     
     context ={'form':form}
     return render(request,"UpdateForm.html", context)