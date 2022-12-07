from django.shortcuts import render, HttpResponse


# Create your views here.

contacts = [
    {
        "nom": "Cassidy",
        "prenom": "Hammond",
        "telephone": "03 94 96 50 97"
    },
    {
        "nom": "Charde",
        "prenom": "Hyde",
        "telephone": "03 44 84 02 60"
    },
    {
        "nom": "Dorian",
        "prenom": "Bailey",
        "telephone": "03 78 24 49 97"
    },
    {
        "nom": "Vivien",
        "prenom": "Duffy",
        "telephone": "03 26 81 80 44"
    },
    {
        "nom": "Ivory",
        "prenom": "Colon",
        "telephone": "03 85 87 65 55"
    }
]

def liste_contacts(request):
    return render(request, 'annuaire/list.html', context={'contacts': contacts})

def fiche_contact(request, nom):
    for contact in contacts :
        if contact['nom']==nom:
            name  = contact['nom']
            first_name = contact['prenom']
            num = contact['telephone']
            return render(request, 'annuaire/contact.html', context={'name': name, 'firstname': first_name, 'num': num})

