"""hse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views
# from django.contrib.auth.views import LoginwebView,LogoutwebView
# from .views import login_view, share_folder_details

urlpatterns = [
    path('', views.loginweb_view, name='loginweb'),
    path('home/', views.vhome, name='nhome'),
    # path('no', views.vhome),
    path('file_update', views.vfileupdate),
    path('api/share-folder-details/', views.share_folder_details_json, name='share_folder_json'),
    path('share-folder-details/', views.share_folder_details_txt, name='share_folder_details_txt'),
    path('map-network-drive/', views.map_network_drive, name='map_network_drive'),
    path('m/',views.vgenerate_bat_menu, name= 'ngenerate_bat_menu'),
    # path('login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),  # Login endpoint
    path('api/', views.handle_request, name='handle_request'),
    path('batconvert/', views.upload_and_process_bat, name='upload_bat'),
    path('api/message/', views.message_handler, name='message_handler'),
    path('arccpc', views.system_info, name='system_info'),  # Endpoint becomes /sharefolder/arccpc
    path('pc-details/', views.pc_details, name='pc_details'),
    path('pc-details/<int:pk>/', views.pc_detail, name='pc_detail'),  # New URL for detail page
    path('pc/<int:pk>/edit-hardware/<int:index>/', views.edit_hardware, name='edit_hardware'),
    path('pc/<int:pk>/delete-hardware/<int:index>/', views.delete_hardware, name='delete_hardware'),
    path('download-pc-details/', views.download_pc_details_excel, name='download_pc_details'),
    path('bat_to_collect_data/', views.vbat_to_collect_data, name='nbat_to_collect_data'),

    path('logoutweb/', views.logoutweb_view, name='logoutweb'),

    path('f/<str:serialnumber>.bat', views.download_bat_files, name='download_bat'),
    path('f/download/<str:data>.bat', views.download_files, name='download_files'),

    path('products/', views.product_list, name='product-list'),



]