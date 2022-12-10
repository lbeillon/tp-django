from django.shortcuts import render

from .models import Contact

# Create your views here.

# contacts = [
#     {
#         "nom": "Cassidy",
#         "prenom": "Hammond",
#         "telephone": "03 94 96 50 97"
#     },
#     {
#         "nom": "Charde",
#         "prenom": "Hyde",
#         "telephone": "03 44 84 02 60"
#     },
#     {
#         "nom": "Dorian",
#         "prenom": "Bailey",
#         "telephone": "03 78 24 49 97"
#     },
#     {
#         "nom": "Vivien",
#         "prenom": "Duffy",
#         "telephone": "03 26 81 80 44"
#     },
#     {
#         "nom": "Ivory",
#         "prenom": "Colon",
#         "telephone": "03 85 87 65 55"
#     }
# ]

#v1 de la liste contact
# def liste_contacts(request):
#     return render(request, 'annuaire/list.html', context={'contacts': contacts})

# version avec la base de données
def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'annuaire/list.html', context={'contacts': contacts})

# liste des particuliers
def liste_particuliers(request):
    contacts = Contact.objects.all()
    particuliers = []
    for contact in contacts :
        if contact.entreprise is False : 
            particuliers.append(contact)
    return render(request, 'annuaire/pages_blanches.html', context={"particuliers": particuliers})

# listes des entreprises
def liste_entreprises(request):
    contacts = Contact.objects.all()
    entreprises = []
    for contact in contacts :
        if contact.entreprise is False : 
            entreprises.append(contact)
    return render(request, 'annuaire/pages_jaunes.html', context={"entreprises": entreprises})

# version fiche contact sans bdd
# def fiche_contact(request, nom):

#     for contact in contacts :
#         if contact['nom']==nom:
#             name  = contact['nom']
#             first_name = contact['prenom']
#             num = contact['telephone']
#     return render(request, 'annuaire/contact.html', context={'name': name, 'firstname': first_name, 'num': num})



# version avec bdd
def fiche_contact(request, nom):
    contacts = Contact.objects.all()
    for contact in contacts :
        if contact.nom ==nom:
            name  = contact.nom
            first_name = contact.prenom
            num = contact.telephone
            return render(request, 'annuaire/contact.html', context={'name': name, 'firstname': first_name, 'num': num})


# fiche particuliers
def fiche_particulier(request, nom):
    contacts = Contact.objects.all()
    for contact in contacts :
        if contact.nom ==nom and contact.entreprise==False:
            name  = contact.nom
            first_name = contact.prenom
            num = contact.telephone
            return render(request, 'annuaire/contact.html', context={'name': name, 'firstname': first_name, 'num': num})