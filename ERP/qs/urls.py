from django.urls import path
from .import views

urlpatterns = [
    path('index',views.vindex,name='nindex'),
    # path('home', views.home, name='home'),
    # path('add-module/', views.add_module, name='nadd_module'),
    # path('edit-module/', views.edit_module, name='edit_module'),
    # path('delete-module/', views.delete_module, name='delete_module'),
]
#  sir when i am running it is showing that template does not exist error
