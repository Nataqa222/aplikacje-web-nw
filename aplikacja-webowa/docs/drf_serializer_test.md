# DRF Serializer Test

## Importy

```python
from myapp.models import Osoba, Stanowisko
from myapp.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io 
```

## Tworzenie stanowiska
```python
stanowisko = Stanowisko.objects.create(nazwa="Developer", opis="Tworzenie aplikacji webowych")
```

#Tworzenie osoby
```python
osoba = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec="M", stanowisko=stanowisko)
```

#Serializacja obiektu Osoba
```python
serializer = OsobaSerializer(osoba)
print(serializer.data)
```

#Serializacja do JSON
```python
content = JSONRenderer().render(serializer.data)
print(content)
```

#Parsowanie JSON
```python
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
```

#Deserializacja
```python
deserializer = OsobaSerializer(data=data)
if deserializer.is_valid():
    print(deserializer.validated_data)
else:
    print(deserializer.errors)
```

#Utrwalenie deserializowanych danych
```python
if deserializer.is_valid():
    deserializer.save()
```