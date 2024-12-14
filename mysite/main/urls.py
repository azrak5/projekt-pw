from django.urls import path
from . import views
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('izdavaci/', IzdavacList.as_view()),
    path('autori/', AutorList.as_view()),
    path('knjige/', KnjigaList.as_view()),
    path('knjige/izdavac/<izdavac>/', IzdavacKnjigaList.as_view()),
    path('knjige/autor/<autor>/', AutorKnjigaList.as_view()),
    path('autori/<drzava>/', AutorDrzavaList.as_view()),
    path('izdavaci/<drzava>/', IzdavacDrzavaList.as_view()),
    path('izdavac/<pk>/', IzdavacDetail.as_view(), name="izdavac-detail"),
    path('autor/<pk>/', AutorDetail.as_view(), name="autor-detail"),
    path('knjiga/<pk>/', KnjigaDetail.as_view(), name='knjiga-detail')
]