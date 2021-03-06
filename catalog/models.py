#! -*- coding=utf8 -*-
from django.db import models
from django.utils.safestring import mark_safe
from django.template import defaultfilters
from unidecode import unidecode
from easy_thumbnails.fields import ThumbnailerImageField

from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)

DEFAULT_PHOTO = "/static/img_sources/default_dish.png"
class Album(models.Model):
    title = models.CharField(max_length=255)
    
    desctiption = models.CharField(max_length=255,blank=True)
    text = models.TextField(blank=True)
    order = models.IntegerField()
    preview= models.OneToOneField('Photo',blank=True,null=True)
    
    slug = models.SlugField(verbose_name=u'URL страницы',
                            help_text=u'Например, uslugi',
                            blank=True,
                            unique=False)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = defaultfilters.slugify(unidecode(self.title))
        return super(Album, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('album-detail-slug', [self.slug])

    def __unidoce__(self):
        return self.title.encode('utf-8')
   # def __str__(self):
   #     return self.title.encode('utf-8')
    def get_prewiew(self):
        if self.preview:
            return self.preview.img['preview'].url
        else:
            return DEFAULT_PHOTO

    class Meta:
        verbose_name=u"Альбом"
        verbose_name_plural=u"Альбомы"
        ordering=["order"]


class News(models.Model):
    title = models.CharField(max_length=255)
    desctiption = models.CharField(max_length=255,blank=True)
    text = models.TextField()
    order = models.IntegerField()
    preview= models.OneToOneField('Photo',blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(verbose_name=u'URL страницы',
                            help_text=u'Например, uslugi',
                            blank=True,
                            unique=False)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = defaultfilters.slugify(unidecode(self.title))
        return super(News, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('news-detail-slug', [self.slug])

    def __unidoce__(self):
        return self.title.encode('utf-8')
   # def __str__(self):
   #     return self.title.encode('utf-8')
    def get_prewiew(self):
        if self.preview:
            return self.preview.img.url
        else:
            return DEFAULT_PHOTO

    class Meta:
        verbose_name=u"Новости"
        verbose_name_plural=u"Новости"
        ordering=["order"]

class Photo(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'название',blank=True)
    descr = models.TextField(verbose_name=u'описание',blank=True)
    img = ThumbnailerImageField(verbose_name=u'фото')
    album_base = models.ForeignKey(Album,verbose_name=u'альбом')

    def get_img(self):
        if self.img:
            return self.img.url
        else:
            return DEFAULT_PHOTO

    def __unicode__(self):
        return self.album_base.title +"/" +self.name
    def save(self,*args,**kwargs):
        if self.name=='':
            self.name = self.img.name
        return super(Photo,self).save(*args,**kwargs)
    class Meta:
        verbose_name=u"фото"
        verbose_name_plural=u"фотографии"
    def admin_t(self):
        return mark_safe(u'<img src="%s" />' % (self.img['preview'].url))
    admin_t.description = 'Thumbnail'
    admin_t.allow_tags = True
