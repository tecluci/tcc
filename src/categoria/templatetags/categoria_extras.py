# -*- coding:utf-8 -*-
from django import template
from django.template.loader import get_template
from django.conf import settings
from src.categoria.models import Category
register = template.Library()

@register.inclusion_tag('category_menu.html')
def show_categories():
    category=Category.objects.filter(parent=None)
    return {'list': category}

@register.inclusion_tag('category_question_list.html')	
def show_categories_id(id):    
    #print id
    category =Category.objects.filter(parent_id=1)
    return {'list': category}

