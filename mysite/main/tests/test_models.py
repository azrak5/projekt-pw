from django.test import TestCase
from main.models import Autor, Knjiga, Izdavac


class Testmodels(TestCase):

    def setUp(self):
        self.autor1 = Autor.objects.create(
            ime = "test-autor",
            adresa = "TestAdresa",
            grad = "TestGrad",
            drzava = "TestDrzava"
        )

        self.izdavac1 = Izdavac.objects.create(
            naziv = "test-izdavac",
            adresa = "TestAdresa",
            grad = "TestGrad",
            drzava = "TestDrzava"
        )

        self.knjiga1 = Knjiga.objects.create(
            naslov = "test-knjiga",
            izdavac = self.izdavac1,
            datum_izdavanja = "2021-12-10"
        )
        self.knjiga1.autor.set([self.autor1])

    def test_author(self):
        self.assertEqual(self.autor1.ime, "test-autor")

    def test_publisher(self):
        self.assertEqual(self.izdavac1.naziv, "test-izdavac")

    def test_book(self):
        self.assertEqual(self.knjiga1.naslov, "test-knjiga")