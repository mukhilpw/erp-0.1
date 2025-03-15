from django.urls import path
from .import views

urlpatterns = [
    path('index',views.vindex,name='nindex'),

]

