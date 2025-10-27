from django.urls import path
from . import views

urlpatterns = [
    path('', views.firapp, name='firstapp'),
    # path('looks', views.looks, name='looks'),

]