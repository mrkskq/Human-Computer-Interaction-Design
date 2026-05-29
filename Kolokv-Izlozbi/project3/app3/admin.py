import datetime

from django.contrib import admin
from .models import *

# Register your models here.

class ExhibitionAdmin(admin.ModelAdmin):
    fields = ['title', 'start_date', 'end_date', 'description', 'location']

    # Изложби и автори може да бидат додадени само од супер-корисници
    def has_add_permission(self, request):
        return request.user.is_superuser

    # Супер-корисниците може да ги гледаат само изложбите што следат, не и тие што се завршени
    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            if obj and obj.end_date >= datetime.date.today():
                return True
        return False

    # Уметниците може да ги прегледаат само изложбите на кои имаат свое дело
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(end_date__gte = datetime.date.today())
        artist = Artist.objects.filter(user = request.user).first()
        if artist:
            return qs.filter(artwork__artist = artist).distinct() # vo Artwork iame artist
        return qs.none()


class ArtistAdmin(admin.ModelAdmin):

    # Изложби и автори може да бидат додадени само од супер-корисници
    def has_add_permission(self, request):
        return request.user.is_superuser


class ArtworkAdmin(admin.ModelAdmin):

    # Уметнички дела можат да бидат додадени само од уметници и уметникот по автоматизам се додава како автор на делото
    def has_add_permission(self, request):
        return Artist.objects.filter(user = request.user).exists()

    def save_model(self, request, obj, form, change):
        artist = Artist.objects.filter(user = request.user).first()
        if not change:
            obj.artist = artist
            obj.save()
        return super().save_model(request, obj, form, change)

    # Делата можат да бидат менувани само од нивите уметници
    def has_change_permission(self, request, obj=None):
        artist = Artist.objects.filter(user = request.user).first()
        if obj and obj.artist == artist:
            return True
        return False





admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
