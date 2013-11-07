from django.contrib import admin
from src.categoria.models import *
from django.utils.datetime_safe import datetime



class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name','description','parent')        
        search_fields = ('name',)
        

admin.site.register(Category, CategoryAdmin)