"""
URL configuration for ERP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.vhome, name='nhome'),
    path('login/', views.vlogin, name='nlogin'),
    path('logout/', views.vlogout, name='nlogout'),
    path('menu/', views.vmenu, name='nmenu'),

    #adminapp for permission and user
    path('adminapp/',include('adminapp.urls')),
    #logdata_and_tel for log data and telegram
    path('logdata_and_tel/',include('logdata_and_tel.urls')),
    
    #hse
    path('hse/',include('hse.urls')),
    #qs
    path('qs/',include('qs.urls')),
    #it
    path('it/',include('it.urls')),

]
