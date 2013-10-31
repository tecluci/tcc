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
    
    name = models.CharField(verbose_name=u"Nome", max_length=50, blank=False, null=False)
    description = models.TextField(verbose_name=u"Descrição", blank=True)
    status = models.CharField(verbose_name=u"Status",max_length=10,blank=False, null=False,choices=STATUS_CHOICES,default='Ativo')
    parent =  models.ForeignKey('self', null=True,blank=True,default=None, related_name='category__self')
    categoria =  models.ForeignKey(Category, null=False,blank=False, related_name='category__categoria')    
    date_joined = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
        
     
    def __unicode__(self):
      return self.name

