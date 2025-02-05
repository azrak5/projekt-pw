from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, IzdavacList, AutorList, KnjigaList, AutorKnjigaList


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:homepage')

        self.assertEqual(resolve(url).func, homepage)

    def test_books_url_is_resolved(self):
        url = reverse('main:knjige')

        self.assertEqual(resolve(url).func.view_class, KnjigaList)

    def test_authors_url_is_resolved(self):
        url = reverse('main:autori')

        self.assertEqual(resolve(url).func.view_class, AutorList)

    def test_authorsbooks_url_is_resolved(self):
        url = reverse('main:knjige_autora', args=['autor'])

        self.assertEqual(resolve(url).func.view_class, AutorKnjigaList)