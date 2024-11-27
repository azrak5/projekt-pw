from django.db import models

# Create your models here.
class Izdavac(models.Model):
    naziv = models.CharField(max_length=30)
    adresa = models.CharField(max_length=50)
    grad = models.CharField(max_length=60)
    drzava = models.CharField(max_length=50)

    def __str__(self):
        return self.naziv
    
class Autor(models.Model):
    ime = models.CharField(max_length=30)
    adresa = models.CharField(max_length=50)
    grad = models.CharField(max_length=60)
    drzava = models.CharField(max_length=50)

    def __str__(self):
        return self.ime

class Knjiga(models.Model):
    naslov = models.CharField(max_length=100)
    authors = models.ForeignKey(Autor, default=1, on_delete=models.CASCADE)
    datum_izdavanja = models.DateField()

    def __str__(self):
        return self.naslov

