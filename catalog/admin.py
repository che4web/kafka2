#! -*- coding=utf8 -*-

from django.contrib import admin
from catalog.models import Album, Photo, News
class PhotosInline(admin.TabularInline):
    model = Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines =  [PhotosInline,]
    list_display=('title','text','order')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
@admin.register(Photo)
class PhotosInline(admin.ModelAdmin):
    pass
    #list_display=('name','descr',)
