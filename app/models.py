#! -*- coding=utf-8 -*-
"""
Definition of models.
"""

from django.db import models

class BasicData(models.Model):
    our_name = models.CharField(max_length=255,verbose_name=u'название на главной странице')
    city = models.TextField(verbose_name=u'город')
    street_home = models.TextField(verbose_name=u'улица_дом')
    tel = models.TextField(verbose_name=u'телефон')
    main_descr = models.TextField(verbose_name=u'главный текст')
    
    def __str__(self):
        return self.our_name
    class Meta:
        verbose_name=u"общие данные"
        verbose_name_plural=u"общие данные"
