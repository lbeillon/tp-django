from django.urls import path
from .views import liste_contacts, hello

urlpatterns = [
    path('annuaire/', hello)
]