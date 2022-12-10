from django.urls import path, re_path
from .views import *

urlpatterns = [
   path('annuaire/', liste_contacts, name='annuaire'),
   path('annuaire/particuliers/', liste_particuliers, name="particuliers"),
   path('annuaire/entreprises/', liste_entreprises, name="entreprises"),

   path('annuaire/<nom>/', fiche_contact, name="contact"),
   path('annuaire/entreprises/<nom>/', fiche_entreprise, name="contact-entreprises"),
   path('annuaire/particuliers/<nom>/', fiche_particulier, name="contact-particuliers"),
   
   
   
]