#! -*- coding=utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from catalog.models import Album

from django.views.generic import ListView, DetailView

def album_list(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalog/album_list.html',
        {
            'title':u'Название какое-то',
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
