## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
class IzdavacFactory(DjangoModelFactory):
    class Meta:
        model = Izdavac

    naziv = factory.Faker("sentence", nb_words=2)
    adresa = factory.Faker("address")
    grad = factory.Faker("city")
    drzava = factory.Faker("country")


class AutorFactory(DjangoModelFactory):
    class Meta:
        model = Autor

    ime = factory.Faker("first_name")
    adresa = factory.Faker("address")
    grad = factory.Faker("city")
    drzava = factory.Faker("country")


class KnjigaFactory(DjangoModelFactory):
    class Meta:
        model = Knjiga

    naslov = factory.Faker("sentence", nb_words=4)
    autor = factory.Iterator(Autor.objects.all())
    izdavac = factory.Iterator(Izdavac.objects.all())
    datum_izdavanja = factory.Faker("date_time")