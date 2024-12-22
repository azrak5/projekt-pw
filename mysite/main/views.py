from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from main.forms import *
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

    def get_queryset(self):
        queryset = super().get_queryset()
        naziv = self.request.GET.get('naziv', None)
        if naziv:
            queryset = queryset.filter(naziv__icontains=naziv)
        return queryset

class AutorList(ListView):
    model = Autor

    def get_queryset(self):
        queryset = super().get_queryset()
        ime = self.request.GET.get('ime', None)
        if ime:
            queryset = queryset.filter(ime__icontains=ime)
        return queryset

class KnjigaList(ListView):
    model = Knjiga

    def get_queryset(self):
        queryset = super().get_queryset()
        autor = self.request.GET.get('autor', None)
        if autor:
            queryset = queryset.filter(autor__ime__icontains=autor)
        return queryset

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

def izd(request):
    if request.method == "POST":
        form = IzdavacForm(request.POST)
        if form.is_valid():
            try:
                izdavac = form.save()
                return redirect('main:izdavac-detail', pk=izdavac.pk)
            except:
                pass
    else:
        form = IzdavacForm()
    return render(request, 'main/izdavac_form.html',{'form':form})

def aut(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            try:
                autor = form.save()
                return redirect('main:autor-detail', pk=autor.pk)
            except:
                pass
    else:
        form = AutorForm()
    return render(request, 'main/autor_form.html',{'form':form})

def knj(request):
    if request.method == "POST":
        form = KnjigaForm(request.POST)
        if form.is_valid():
            try:
                knjiga = form.save()
                return redirect('main:knjiga-detail', pk=knjiga.pk)
            except:
                pass
    else:
        form = KnjigaForm()
    return render(request, 'main/knjiga_form.html',{'form':form})

def editizd(request, id):
    izdavac = Izdavac.objects.get(id=id)
    return render(request, 'main/editizd.html', {'izdavac':izdavac})

def updateizd(request, id):
    izdavac = Izdavac.objects.get(id=id)
    form = IzdavacForm(request.POST, instance=izdavac)
    if form.is_valid():
        form.save()
        return redirect('main:izdavac-detail', pk=izdavac.pk)
    return render(request, 'main/editizd.html', {'izdavac': izdavac})

def editaut(request, id):
    autor = Autor.objects.get(id=id)
    return render(request, 'main/editaut.html', {'autor':autor})

def updateaut(request, id):
    autor = Autor.objects.get(id=id)
    form = AutorForm(request.POST, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('main:autor-detail', pk=autor.pk)
    return render(request, 'main/editaut.html', {'autor': autor})

def editknj(request, id):
    knjiga = Knjiga.objects.get(id=id)
    autori = Autor.objects.all()
    izdavaci = Izdavac.objects.all()
    return render(request, 'main/editknj.html', {
        'knjiga': knjiga,
        'autori': autori,
        'izdavaci': izdavaci
    })

def updateknj(request, id):
    knjiga = Knjiga.objects.get(id=id)
    form = KnjigaForm(request.POST, instance=knjiga)
    if form.is_valid():
        form.save()
        return redirect('main:knjiga-detail', pk=knjiga.pk)
    return render(request, 'main/editknj.html', {'knjiga': knjiga})

def deleteizd(request, id):
    izdavac = Izdavac.objects.get(id=id)
    izdavac.delete()
    return redirect("../izdavaci/")

def deleteaut(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect("../autori/")

def deleteknj(request, id):
    knjiga = Knjiga.objects.get(id=id)
    knjiga.delete()
    return redirect("../knjige/")