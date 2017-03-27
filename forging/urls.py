#! -*- coding=utf-8 -*-
"""
Definition of urls for forging.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from catalog import views
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

import app.forms
import app.views
import catalog.views

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^catalog/$', catalog.views.album_list, name='catalog'),
    url(r'^catalog/(?P<slug>.+)/$', catalog.views.AlbumDetailView.as_view(), name='album-detail-slug'),
    url(r'^catalog/(?P<pk>\d+)/$', catalog.views.AlbumDetailView.as_view(), name='album-detail'),
    url(r'^news/$', catalog.views.news_list, name='news-list'),
    url(r'^news/(?P<slug>.+)/$', catalog.views.NewsDetailView.as_view(), name='news-detail-slug'),
    url(r'^news/(?P<pk>\d+)/$', catalog.views.NewsDetailView.as_view(), name='news-detail'),
    url(r'^sender/$', catalog.views.ContactFormView.as_view(), name='sender'),
    #url(r'^news2$', views.NewsListView.as_view(), name='news-list2'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
