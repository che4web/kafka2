#! -*- coding=utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import HttpResponse
import json
from django.http import HttpResponseBadRequest

from datetime import datetime
from catalog.models import Album, News

from django.views.generic import ListView, DetailView, FormView
from catalog.forms import ContactForm


def album_list(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalog/album_list.html',
        {
            'title':u'Кованые изделия перми. Галерея наших работ',
            'page_title':u' Галерея наших работ',
            'object_list': Album.objects.all()
        }
    )
def news_list(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalog/news_list.html',
        {
            'title':u'Кованые изделия перми. Новости нашей компании',
            'page_title':u' Новости',
            'object_list': News.objects.all()
        }
    )
#class NewsListView(ListView):
#    model = Album
#    def get_context_data(self, **kwargs):
#        context = super(NewsListView, self).get_context_data(**kwargs)
#        context['title']= u'Наши новости и события'
#        return context

#class NewsListView(ListView):
#    model = Album
#    def get_context_data(self, **kwargs):
#        context = super(NewsListView, self).get_context_data(**kwargs)
#        context['title']= u'Наши новости и события'
#        return context

class AlbumDetailView(DetailView):
    model = Album

    def get_context_data(self, *args,**kwargs):
        context= super(AlbumDetailView,self).get_context_data(*args,**kwargs)
        context['title'] =  u'Кованые изделия перми. Галерея наших работ: '+ self.object.title
        context['page_title'] =  self.object.title
        context['desctiption'] =  self.object.desctiption 
        return context

class NewsDetailView(DetailView):
    model = News

class ContactFormView(FormView):
    form_class=ContactForm
    template_name='contact.html'

    def form_valid(self,form):
        form.send_email()
        return HttpResponse('Ok')

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))
