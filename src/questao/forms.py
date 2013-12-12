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
		self.fields['resposta'].widget.attrs['class'] = 'radiox'

	CHOICES_BOOLEAN = (
		(0,u'Não'),
		(1,u'Sim'),
	)
	
	resposta = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES_BOOLEAN)	

class RespostaFilhoForm(forms.ModelForm):
	class Meta:
		model = Resposta
		exclude = ('date_joined',)		

	def __init__(self, *args, **kwargs):
		super(RespostaFilhoForm, self).__init__(*args, **kwargs)		
		self.fields['questao'].widget = forms.HiddenInput()	
		
	resposta = forms.ChoiceField(widget=forms.RadioSelect,choices=RESPOSTA_CHOICES)		