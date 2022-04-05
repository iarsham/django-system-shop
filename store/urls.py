from django.urls import path
from .views import *

urlpatterns = [
    path('category/', category, name='category'),
    path('product-detail/<str:pk>/', product_detail, name='detail-products'),
    ]
