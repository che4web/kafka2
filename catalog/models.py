#! -*- coding=utf8 -*-
from django.db import models

#DEFAULT_PHOTO = "/static/img_sources/default_dish.png"
class Album(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    order = models.IntegerField()

    @models.permalink
    def get_absolute_url(self):
        return ('album-detail', [self.id])
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name=u"Альбом"
        verbose_name_plural=u"Альбомы"
        ordering=["order"]

#class Photo(models.Model):
#    name = models.CharField(max_length=255,verbose_name=u'название')
#    descr = models.TextField(verbose_name=u'описание')
#    img = models.ImageField(blank=True,verbose_name=u'фото блюда')
#    category = models.ForeignKey(Album,verbose_name=u'альбом')   
    
#    @models.permalink
#    def get_absolute_url(self):
#        return ('menu-detail', [self.id])

#    def get_img(self):
#        if self.img:
#            return self.img.url
#        else:
#            return DEFAULT_PHOTO

#    class Meta:
#        verbose_name=u"фото"
#        verbose_name_plural=u"фотографии"
