from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Osoba, Stanowisko  # Import modeli

# Widok powitalny
def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas: {now}.
        </body></html>"""
    return HttpResponse(html)

# Nowy widok listy osób
def person_list(request):
    osoby = Osoba.objects.all()
    return render(request, "myapp/person/list.html", {'osoby': osoby})

# Nowy widok szczegółów osoby
def person_detail(request, id):
    try:
        osoba = Osoba.objects.get(id=id)
    except Osoba.DoesNotExist:
        return render(request, "myapp/person/not_found.html", status=404)
    return render(request, "myapp/person/detail.html", {'osoba': osoba})

# Nowy widok listy stanowisk
def team_list(request):
    stanowiska = Stanowisko.objects.all()
    return render(request, "myapp/team/list.html", {'stanowiska': stanowiska})

# Nowy widok szczegółów stanowiska
def team_detail(request, id):
    try:
        stanowisko = Stanowisko.objects.get(id=id)
    except Stanowisko.DoesNotExist:
        return render(request, "myapp/team/not_found.html", status=404)
    return render(request, "myapp/team/detail.html", {'stanowisko': stanowisko})
