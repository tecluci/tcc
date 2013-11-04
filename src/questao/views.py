# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from src.categoria.models import Category
from src.questao.models import *


def home(request):
    data = {
        
    }

    return render_to_response('questao/home.html', data, context_instance=RequestContext(request))


def questionario(request):
    category=Category.objects.all()
    data = {
        "category":category,
    }

    return render_to_response('questao/perguntas.html', data, context_instance=RequestContext(request))
