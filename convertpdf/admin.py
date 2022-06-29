from django.contrib import admin
from . models import *
# Register your models here.

class Prewiew(admin.ModelAdmin):
    list_display = ("name", "pdf_file")
    list_per_page = 10
admin.site.register(Storage,Prewiew)
