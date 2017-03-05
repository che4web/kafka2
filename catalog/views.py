#! -*- coding=utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from catalog.models import Album, News

from django.views.generic import ListView, DetailView

def album_list(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalog/album_list.html',
        {
            'title':u'Кованые изделия перми. Гелерея наших работ',
            'object_list': Album.objects.all()
        }
    )
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
        context['title'] =  u'Кованые изделия перми. Гелерея наших работ: '+ self.object.title
        return context

class NewsDetailView(DetailView):
    model = News
