from catalog.models import Album
def album_list(request):
    return {'album_list':Album.objects.all()}
