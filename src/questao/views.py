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


def questionario(request,id):
    category=Category.objects.filter(id=id)
    
    category_children=Category.objects.filter(parent_id=id)

    category_children2 = []
    for x in category_children:
		category_children2.append([x,Category.objects.filter(parent_id=x.id)])
		
    print category_children2

    data = {
        "category":category_children2,
    }

    return render_to_response('questao/perguntas.html', data, context_instance=RequestContext(request))

def recursive_category(hierarchy):
    children = hierarchy_parent.objects.filter(parent_id=_hierarchy)
    if children.count():
        for x in children:
            temp = self.recursive_last_level_hierarchy(x.hierarchy_id)
        return temp
    else:
        #caso não exista ele add a lista pq é o o ultimo nivel da hierarquia
        self.hierarchy_list.append(int(_hierarchy))
        return self.hierarchy_list