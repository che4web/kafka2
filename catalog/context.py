# -*- coding:utf8 -*-
from catalog.models import Album
def album_list(request):
    return {'album_list':Album.objects.all(),
            'description_d':u'Ходуожественная ковка в перми. Изготовление кованых изделий на заказ. Качественные кованые изделия по разумной цене'
            }
