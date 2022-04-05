from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', add_order, name='checkout'),
    path('contact/', contact, name='contact'),
]
