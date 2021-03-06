# -*- coding:utf-8 -*-
from django.db import models
from src.categoria.models import Category


class Questao(models.Model):
    
    class Meta:
       verbose_name = 'Questao'

    
    STATUS_CHOICES = (
      (u'Ativo', u'Ativo'),
      (u'Inativo', u'Inativo'),
    )
    
    name = models.TextField(verbose_name=u"Pergunta", blank=False, null=False)
    status = models.CharField(verbose_name=u"Status",max_length=10,blank=False, null=False,choices=STATUS_CHOICES,default='Ativo')
    parent =  models.ForeignKey('self', null=True,blank=True,default=None, related_name='category__self')
    categoria =  models.ForeignKey(Category, null=True,blank=True,default=None, related_name='category__categoria')    
    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
        
     
    def __unicode__(self):
      return self.name
      
RESPOSTA_CHOICES = (
      (0, u'Atividade Ausente'),
      (1, u'Atividade Parcialmente Ausente'),
      (2, u'Atividade Parcialmente Presente'),
      (3, u'Atividade Presente'),
    )
class Resposta(models.Model):
    
    class Meta:
       verbose_name = 'Resposta'

    
    resposta = models.CharField(verbose_name=u"Pergunta", blank=False, null=False,max_length=30)
    skey = models.CharField(blank=True, null=True,max_length=255)
    questao =  models.ForeignKey(Questao, null=False,blank=False, related_name='questao__resposta')    
    date_joined = models.DateTimeField(auto_now=True)
     
    def __unicode__(self):
      return self.resposta
