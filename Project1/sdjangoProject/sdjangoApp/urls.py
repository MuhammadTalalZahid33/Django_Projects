from django.urls import path
from . import views

urlpatterns = [
    path('', views.subHome, name='subhome'),
    
]