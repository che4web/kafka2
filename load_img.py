#! -*- coding=utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from catalog.models import Photo, Album
from django.core.files import File
from os import listdir

PATH ='D:/web-dev/tmp/kaffka-photos/z'
ls = listdir(PATH)
order = len(Album.objects.all())
album = Album.objects.get(id=23)
order=order+1
photo_ls =  listdir(PATH)
for name in photo_ls:
    img = u''+PATH +'/'+name
    f=File(open(img.decode('utf-8'),'r'))
    photo = Photo(name=name.decode('utf-8'),
    album_base=album)
    photo.img.save(name,f)
    photo.save()

