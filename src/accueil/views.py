from django.shortcuts import render

from datetime import datetime

def helloworld(request):
    return render(request, "accueil/helloworld.html", context={"date": datetime.today()})

def somme(request, num1, num2):
    somme = int(num1) + int(num2)
    return render(request, "accueil/sum.html", context={"somme": somme})
