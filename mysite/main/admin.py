from django.contrib import admin
from .models import *

# Register your models here.
model_list = [Knjiga, Autor, Izdavac]
admin.site.register(model_list)
