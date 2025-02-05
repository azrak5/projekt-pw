from django.test import TestCase, Client
from django.urls import reverse
from main.models import Autor, Izdavac


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:homepage')
        self.authors_q_url = reverse('main:knjige_autora', args=['test-autor'])
        self.publishers_q_url = reverse('main:knjige_izdavaca', args=['test-izdavac'])

        self.autor1 = Autor.objects.create(
            ime = 'test-autor',
            adresa = 'TestAdress',
            grad = 'TestCity',
            drzava = 'TestCountry'
        )

        self.izdavac1 = Izdavac.objects.create(
            naziv = "test-izdavac",
            adresa = "TestAdresa",
            grad = "TestGrad",
            drzava = "TestDrzava"
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

    def test_project_authors_GET(self):
        client = Client()

        response = client.get(self.authors_q_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/knjiga_autor.html')

    def test_project_publishers_GET(self):
        client = Client()

        response = client.get(self.publishers_q_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/knjiga_izdavac.html')