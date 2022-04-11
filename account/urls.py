from django.urls import path
from .views import *

urlpatterns = [
    path('login/', auth_login, name='login'),
    path('signup/', auth_signup, name='signup'),
    path('logout/', auth_logout, name='logout'),
    path('activate/<uidb64>/<token>/', auth_activate, name='activate'),
    # Password Reset
    path('reset_done/', forget_password, name='reset_mail'),
    path('reset_validate/<uidb64>/<token>/', resetpassword_validate, name='reset_validate'),
    path('password_reset/', password_reset, name='password_reset')
]
