from django.shortcuts import render


def base(request):
    return render(request, "layouts/base.html")