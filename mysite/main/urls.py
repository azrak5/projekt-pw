from django.urls import path
from . import views
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('izdavaci/', IzdavacList.as_view()),
    path('autori/', AutorList.as_view(), name='autori'),
    path('knjige/', KnjigaList.as_view(), name='knjige'),
    path('knjige/izdavac/<izdavac>/', IzdavacKnjigaList.as_view(), name='knjige_izdavaca'),
    path('knjige/autor/<autor>/', AutorKnjigaList.as_view(), name='knjige_autora'),
    path('autori/<drzava>/', AutorDrzavaList.as_view()),
    path('izdavaci/<drzava>/', IzdavacDrzavaList.as_view()),
    path('izdavac/<pk>/', IzdavacDetail.as_view(), name="izdavac-detail"),
    path('autor/<pk>/', AutorDetail.as_view(), name="autor-detail"),
    path('knjiga/<pk>/', KnjigaDetail.as_view(), name="knjiga-detail"),
    path('addizdavac/', views.izd),
    path('addautor/', views.aut),
    path('addknjiga/', views.knj),
    path('editizd/<int:id>', views.editizd),
    path('updateizd/<int:id>', views.updateizd),
    path('editaut/<int:id>', views.editaut),
    path('updateaut/<int:id>', views.updateaut),
    path('editknj/<int:id>', views.editknj),
    path('updateknj/<int:id>', views.updateknj),
    path('deleteizd/<int:id>', views.deleteizd),
    path('deleteaut/<int:id>', views.deleteaut),
    path('deleteknj/<int:id>', views.deleteknj)
]