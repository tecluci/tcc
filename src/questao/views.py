# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
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
    #print request.session.session_key
    category_children=Category.objects.filter(parent_id=id)

    for x in category_children:
	    x.children  = Category.objects.filter(parent_id=x.id)
	    for w in x.children:
	    	w.questao = Questao.objects.filter(Q(categoria_id=w.id) & Q(parent_id=None))
	    	#listando questoes pai
	    	for q in w.questao:	    		
	    		#add form pai a questao pai
	    		#verifica se existe respota no banco de dados
	    		try:
	    			r = Resposta.objects.get(Q(questao=q) & Q(skey=request.session.session_key))
	    			q.form = RespostaPaiForm(instance=r)
	    			q.resposta = r
	    			
	    		except:
	    			q.form = RespostaPaiForm(initial={"questao":q})

	    		#add questoes filho a variavel
	    		q.questao_filho = Questao.objects.filter(Q(parent_id=q.id))
	    		for qw in q.questao_filho:
	    			try:
		    			rw = Resposta.objects.get(Q(questao=qw) & Q(skey=request.session.session_key))
		    			qw.form = RespostaFilhoForm(instance=rw)
		    			qw.resposta = rw	    			
		    		except:		    			
	    				qw.form = RespostaFilhoForm(initial={"questao":qw})

    data = {
        "category":category_children,
        'cat_id':id,
    }

    return render_to_response('questao/perguntas.html', data, context_instance=RequestContext(request))

from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.html import escape

def senderpost(request):
	if request.POST: #verifica se existe POST		
		saved = False
		try:
			r = Resposta.objects.get(Q(questao_id=request.POST['questao']) & Q(skey=request.session.session_key))
			form = RespostaPaiForm(request.POST, instance=r)
			saved = True			
					
		except:		
			saved = True	
			form = RespostaPaiForm(request.POST) #chama o form dos forms.py e add os dados do POST
			r = None
		#print request.session.session_key
		if form.is_valid() and saved:
			form_s = form.save(commit=False)
			form_s.skey = request.session.session_key
			form_s.save()
			msg = " salvo %s"%naturaltime(form_s.date_joined)
			response = HttpResponse(escape(msg))
				

			return response
		
			

	
	return HttpResponse('salvo')

def senderpost2(request):
	if request.POST: #verifica se existe POST		
		try:
			r = Resposta.objects.get(Q(questao_id=request.POST['questao']) & Q(skey=request.session.session_key))
			form = RespostaFilhoForm(request.POST, instance=r)
		except:			
			form = RespostaFilhoForm(request.POST) #chama o form dos forms.py e add os dados do POST
			r = None
		if form.is_valid(): 			
			form_s = form.save(commit=False)
			form_s.skey = request.session.session_key
			form_s.save()
			
			r_list = []
			r = Resposta.objects.get(Q(questao_id=form_s.questao_id) & Q(skey=request.session.session_key))
			if r:
				for x in Questao.objects.filter(Q(parent_id=r.questao.parent_id)):
					try:
						res = Resposta.objects.get(Q(questao=x) & Q(skey=request.session.session_key))		
						r_list.append(int(res.resposta))
					except:	
						r_list.append(0)
				media = sum(r_list) / float(len(r_list))
				
				Resposta.objects.filter(Q(questao__id=r.questao.parent_id)).update(resposta=media)
				
			msg = " salvo %s"%naturaltime(form_s.date_joined)
			response = HttpResponse(escape(msg))
			return response

	
	return HttpResponse('ok')


def report(request,id_cat):
	category_children=[v.id for v in Category.objects.filter(parent_id=id_cat)]
	category_children2=[v.id for v in Category.objects.filter(parent_id__in=category_children)]
	q = Questao.objects.filter(Q(categoria_id__in=category_children2) & Q(parent_id=None))
	
	nquestoes = q.count()
	r_list = []
	
	soma = 0

	
	for x in q:		
		
		try:
			res = Resposta.objects.get(Q(questao=x) & Q(skey=request.session.session_key))
			re = res.resposta
			r_list.append(float(re))	
		except:	
			re = 0
			r_list.append(re)
	soma = sum(r_list)
	pontuacao_maxima = nquestoes*3	
	percent = int(round((soma*100)/pontuacao_maxima))
	
	data = {
        "category":Category.objects.get(id=id_cat),        
        'media':percent,

    }	
	return render_to_response('questao/relatorio.html', data, context_instance=RequestContext(request))

