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
      

class Resposta(models.Model):
    
    class Meta:
       verbose_name = 'Resposta'

    
    RESPOSTA_CHOICES = (
      (1, u'Atividade Ausente'),
      (2, u'Atividade Parcialmente Ausente'),
      (3, u'Atividade Parcialmente Presente'),
      (4, u'Atividade Presente'),
    )
    
    resposta = models.CharField(verbose_name=u"Pergunta", blank=False, null=False,max_length=30,choices=RESPOSTA_CHOICES)
    questao =  models.ForeignKey(Questao, null=False,blank=False, related_name='questao__resposta')    
    date_joined = models.DateTimeField(auto_now_add=True)
     
    def __unicode__(self):
      return self.resposta
