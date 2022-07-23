from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('info/<int:pk>/', views.productdetail, name='productdetail'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
]