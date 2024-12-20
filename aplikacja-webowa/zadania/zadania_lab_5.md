# Rozwiązania zadań lab 5

## Zadanie 1
Dodanie 3 obiektów typu `Person` i `Team` w Django shell:
```python
from myapp.models import Person, Team

team1 = Team.objects.create(nazwa="Team Alpha", opis="Zespół pierwszy")
team2 = Team.objects.create(nazwa="Team Beta", opis="Zespół drugi")
team3 = Team.objects.create(nazwa="Team Gamma", opis="Zespół trzeci")

person1 = Person.objects.create(imie="Anna", nazwisko="Nowak", plec="K", stanowisko=team1)
person2 = Person.objects.create(imie="Bartek", nazwisko="Kowalski", plec="M", stanowisko=team2)
person3 = Person.objects.create(imie="Cezary", nazwisko="Wiśniewski", plec="M", stanowisko=team3)
