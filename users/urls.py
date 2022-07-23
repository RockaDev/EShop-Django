from django.urls import path

from . import views

urlpatterns = [
    path('loading/', views.loading_data, name='loading_data'),
    path('', views.home, name='home'),
    path('admin-login/', views.adminlogin, name='adminlogin'),
    path('logout/', views.logout, name='logout'),
]