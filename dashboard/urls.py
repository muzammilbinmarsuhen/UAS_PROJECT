from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('produk/',views.produk,name='produk'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('order_create/', views.orderCreate,name='order_create'),
    path('update_create/<str:pk>/', views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder,name='delete_order'),
]