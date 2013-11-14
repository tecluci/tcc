# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from src.categoria.models import Category
from src.questao.models import *
from src.questao.forms import *
from django.db.models import Q


def home(request):
    
    data = {
    
    }

    return render_to_response('questao/home.html', data, context_instance=RequestContext(request))


def questionario(request,id):
    category=Category.objects.filter(id=id)
    
    category_children=Category.objects.filter(parent_id=id)

    for x in category_children:
	    x.children  = Category.objects.filter(parent_id=x.id)
	    for w in x.children:
	    	w.questao = Questao.objects.filter(Q(categoria_id=w.id) & Q(parent_id=None))
	    	#listando questoes pai
	    	for q in w.questao:
	    		#add questoes filhho a variavel
	    		q.questao_filho = Questao.objects.filter(Q(parent_id=q.id))
	    		#add form pai a questao pai
	    		q.form = RespostaPaiForm(initial={"questao":q})
	    		#w.form = RespostaFilhoForm()

    data = {
        "category":category_children,
    }

    return render_to_response('questao/perguntas.html', data, context_instance=RequestContext(request))

