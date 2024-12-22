from django import forms  
from main.models import *

class IzdavacForm(forms.ModelForm):  
    class Meta:  
        model = Izdavac  
        fields = "__all__"

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = "__all__"

class KnjigaForm(forms.ModelForm):
    class Meta:
        model = Knjiga
        fields = "__all__"
  