from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from main.models import *

## Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:homepage')
    else:
        form = UserCreationForm()
    
    context = {'form': form}

    return render(request, 'registration/register.html', context)

class IzdavacList(ListView):
    model = Izdavac

class AutorList(ListView):
    model = Autor

class KnjigaList(ListView):
    model = Knjiga

class IzdavacKnjigaList(ListView):
    template_name = 'main/knjiga_izdavac.html'

    def get_queryset(self):
        self.izdavac = get_object_or_404(Izdavac, naziv=self.kwargs['izdavac'])
        return Knjiga.objects.filter(izdavac=self.izdavac)
    
class AutorKnjigaList(ListView):
    template_name = 'main/knjiga_autor.html'

    def get_queryset(self):
        self.autor = get_object_or_404(Autor, ime=self.kwargs['autor'])
        return Knjiga.objects.filter(autor=self.autor)
    
class AutorDrzavaList(ListView):
    template_name = 'main/autor_drzava.html'

    def get_queryset(self):
        return Autor.objects.filter(drzava=self.kwargs['drzava'])
    
class IzdavacDrzavaList(ListView):
    template_name = 'main/izdavac_drzava.html'

    def get_queryset(self):
        return Izdavac.objects.filter(drzava=self.kwargs['drzava'])
    
class IzdavacDetail(DetailView):
    model = Izdavac

class AutorDetail(DetailView):
    model = Autor

class KnjigaDetail(DetailView):
    model = Knjiga