from django.contrib import admin
from .models import Paradigm,Language,Programmer

# Register your models here.
admin.site.register(Language)
admin.site.register(Programmer)
admin.site.register(Paradigm)