from django.urls import path
from . import views

urlpatterns = [
    path('cart-view', views.cart_view, name='cart-view'),
    path('add-cart/<str:pk>/', views.add_cart, name='add-cart'),
    path('remove-cart/<str:pk>/', views.remove_cart, name='remove-cart'),
]
