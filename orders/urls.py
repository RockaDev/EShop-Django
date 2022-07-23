from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.placed_order, name='placed_order'),
    path('error404/', views.no_permissions, name='no_permissions'),
    path('order/<int:pk>/', views.orderdetail, name='orderdetail'),
]