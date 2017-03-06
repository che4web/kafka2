#! -*- coding=utf-8 -*-
"""
Definition of views.
"""
from app import forms
from app import models

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import BasicData
from catalog.models import News, Album

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Изготовление кованых изделий на заказ в перми. Ковкa Пермь',
            'year':datetime.now().year,
            'basicdata':BasicData.objects.all()[0],
            'news_list':News.objects.all(),
            'albums_list':Album.objects.all(),
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
