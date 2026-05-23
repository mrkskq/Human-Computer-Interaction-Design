from django.contrib import admin
from django.db.models import Count

from .models import *

# Register your models here.

class TouristGuideAdmin(admin.ModelAdmin):

    # Туристички водичи можат да бидат додени, менувани и бришени само од супер-корисници
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    # На супер-корисниците во Админ панелот им се прикажуваат само туристичките водачи со помалку од 3 дестинации
    # vo Travel cuvame "guide", ama se prajt i povratna relacija Travel <-> TouristGuide,
    # zato "travel" e related_name po default, t.e mojme da go pristapime od TouristGuide, iako tamu ne cuvame "travel"
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(travels_count = Count('travel')).filter(travels_count__lt=3)
        return qs


class TravelAdmin(admin.ModelAdmin):

    fields = ['destination', 'price', 'duration', 'image']

    def save_model(self, request, obj, form, change):
        guide = TouristGuide.objects.filter(user = request.user).first()
        travels = Travel.objects.filter(guide = guide).all()

        total_price = 0
        for travel in travels:
            total_price += travel.price

        if not change:

            # Еден туристички водич може да има максимум 5 дестинации во дадено време
            if travels.count() >= 5:
                return

            # Вкупната цена на дестинациите на еден туристички водач не смее да надминува 50 000.
            if total_price + obj.price > 50000:
                return

            # Туристички водач не може да додаде дестинација, ако веќе постои дестинација со тоа име
            if Travel.objects.filter(destination = obj.destination).exists():
                return

        super().save_model(request, obj, form, change)

    # Дестинациите можат да бидат менувани само од туристичките водачи кои се задолжени за таа дестинација, а останатите туристички водачи може само да ги гледаат тие дестинации
    def has_change_permission(self, request, obj = None):
        return obj and obj.guide.user == request.user


admin.site.register(TouristGuide, TouristGuideAdmin)
admin.site.register(Travel, TravelAdmin)