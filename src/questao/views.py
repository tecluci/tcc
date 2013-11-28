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
    print request.session.session_key
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
	    			qw.form = RespostaFilhoForm(initial={"questao":qw})

    data = {
        "category":category_children,
    }

    return render_to_response('questao/perguntas.html', data, context_instance=RequestContext(request))

from django.contrib.humanize.templatetags.humanize import naturaltime
def senderpost(request):
	if request.POST: #verifica se existe POST		
		form = RespostaPaiForm(request.POST) #chama o form dos forms.py e add os dados do POST
		print request.session.session_key
		if form.is_valid: 			
			form_s = form.save(commit=False)
			form_s.skey = request.session.session_key
			form_s.save()
			msg = "<span class='glyphicon glyphicon-ok'></span> salvo %s"%naturaltime(form_s.date_joined)
			response = HttpResponse(msg,content_type="application/liquid")
			response['Content-Length'] = len(msg)

			return response

	
	return HttpResponse('ok')

def senderpost2(request):
	if request.POST: #verifica se existe POST		
		form = RespostaFilhoForm(request.POST) #chama o form dos forms.py e add os dados do POST
		
		if form.is_valid: 			
			form_s = form.save(commit=False)
			form_s.skey = request.session.session_key
			form_s.save()
			return HttpResponse('1')

	
	return HttpResponse('ok')
