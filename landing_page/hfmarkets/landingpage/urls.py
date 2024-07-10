# landingpage/urls.py

from django.urls import path
from . import views
from .views import home

urlpatterns = [    
    path('', home, name='home'),
    path('register/', views.register, name='register'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
