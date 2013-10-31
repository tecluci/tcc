from django.contrib import admin
from src.questao.models import *
from django.utils.datetime_safe import datetime



class QuestaoAdmin(admin.ModelAdmin):
        list_display = ('name','description')        
        search_fields = ('name',)
        

admin.site.register(Questao, QuestaoAdmin)