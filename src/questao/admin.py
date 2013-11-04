from django.contrib import admin
from src.questao.models import *
from django.utils.datetime_safe import datetime



class QuestaoAdmin(admin.ModelAdmin):
        list_display = ('name',)        
        search_fields = ('name',)
        

admin.site.register(Questao, QuestaoAdmin)

class RespostaAdmin(admin.ModelAdmin):
        list_display = ('resposta',)        
        search_fields = ('resposta',)
        

admin.site.register(Resposta, RespostaAdmin)