from django.urls import path
from .import views

urlpatterns = [
    path('',views.vhome,name='nhome'),
]
#  sir when i am running it is showing that template does not exist error
