#! -*- coding=utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from catalog.models import Photo, Album
from django.core.files import File
from os import listdir

PATH ='/home/che/svn/kafka_img'
ls = listdir(PATH)
order = len(Album.objects.all())
for dr in ls:
    album = Album(title=dr,order=order)

    album.save()
    order=order+1
    photo_ls = listdir(PATH+'/'+dr)
    print dr
    for name in photo_ls:
        img = u''+PATH +'/' +dr+'/'+name
        f=File(open(img.decode('utf-8'),'r'))
        photo = Photo(name=name.decode('utf-8'),
                      album_base=album)
        photo.img.save(name,f)
        photo.save()

