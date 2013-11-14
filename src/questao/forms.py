# -*- coding:utf-8 -*-
from django import forms
from src.categoria.models import Category
from src.questao.models import *
from django.db.models import Q

class RespostaPaiForm(forms.ModelForm):
	class Meta:
		model = Resposta
		exclude = ('date_joined',)

	
	def __init__(self, *args, **kwargs):
		super(RespostaPaiForm, self).__init__(*args, **kwargs)		
		self.fields['questao'].widget = forms.HiddenInput()	

	CHOICES_BOOLEAN = (
		(0,u'Não'),
		(4,u'Sim'),
	)
	
	resposta = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES_BOOLEAN)	

class RespostaFilhoForm(forms.ModelForm):
	class Meta:
		model = Resposta
		exclude = ('date_joined',)		