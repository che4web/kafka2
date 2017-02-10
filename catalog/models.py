#! -*- coding=utf8 -*-
from django.db import models

DEFAULT_PHOTO = "/static/img_sources/default_dish.png"
class Album(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    order = models.IntegerField()
    preview= models.OneToOneField('Photo',blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('album-detail', [self.id])

    def __unidoce__(self):
        return self.title.encode('utf-8')
    def __str__(self):
        return self.title.encode('utf-8')
    class Meta:
        verbose_name=u"Альбом"
        verbose_name_plural=u"Альбомы"
        ordering=["order"]

class Photo(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'название',blank=True)
    descr = models.TextField(verbose_name=u'описание',blank=True)
    img = models.ImageField(verbose_name=u'фото')
    album_base = models.ForeignKey(Album,verbose_name=u'альбом')

    def get_img(self):
        if self.img:
            return self.img.url
        else:
            return DEFAULT_PHOTO

    class Meta:
        verbose_name=u"фото"
        verbose_name_plural=u"фотографии"
