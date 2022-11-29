from django.urls import path
from .views import helloworld, somme

urlpatterns = [
    path('', helloworld, name='accueil'),
    path('<num1>/<num2>/', somme, name='somme'),
]