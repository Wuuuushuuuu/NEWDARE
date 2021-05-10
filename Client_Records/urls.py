"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import home_view
from pages.views import Login_view_dentist
from pages.views import Contact_view
from pages.views import Login_view_client
from pages.views import Register_view
from django.views.generic.base import TemplateView
from django.conf.urls import url
urlpatterns = [

    
    path("", home_view, name="home"),
    path("Home/", home_view, name="home"),
    path('Dentist_Login/', Login_view_dentist, name ="Login"),
    path('Contact/', Contact_view, name="contact"),
    path('user_login/', Login_view_client, name ="BK1_Login_client"),
    path('Regisyer_user/', Register_view, name="Register"),
    #path("", include("hello.urls")),
    path('admin/', admin.site.urls)
]
