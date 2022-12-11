from django.urls import path, re_path
from .views import helloworld, somme

urlpatterns = [
    path('accueil/', helloworld, name='accueil'),
    path('somme/<num1>/<num2>/', somme, name='somme'),
    re_path(r'somme_regex/(?P<num1>\d+)/(?P<num2>\d+)', somme, name="somme-regex"),
]