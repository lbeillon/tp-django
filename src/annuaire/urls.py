from django.urls import path, re_path
from .views import *

urlpatterns = [
   path('annuaire/', liste_contacts, name='annuaire'),
   path('annuaire/<nom>/<prenom>/', fiche_contact, name="contact")
]