from django.contrib import admin
from django.db.models import Count

from .models import *

# Register your models here.

class BakerAdmin(admin.ModelAdmin):

    # Пекарите можат да бидат додадени, менувани и бришени само од супер-корисници.
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj = None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser

    # На супер-корисниците во Админ панелот им се прикажуваат пекарите со помалку од 5 торти.
    # vo Cake modelot cuvame "baker", ama se prajt i povratna relacija Cake <-> Baker, zato "cake" e related_name po default
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cakes_count = Count('cake')).filter(cakes_count__lt=5)
        return qs


class CakeAdmin(admin.ModelAdmin):

    fields = ['name', 'price', 'weight', 'description', 'image' ,'baker']

    def save_model(self, request, obj, form, change):
        baker = Baker.objects.filter(user = request.user).first()
        baker_cakes = Cake.objects.filter(baker = baker).all()

        # Еден пекар може да има максимум 10 торти во дадено време.
        if not change and baker_cakes.count() >= 10:
            return

        # Вкупната цена на тортите на еден пекар не смее да надминува 10 000.
        total = 0
        for cake in baker_cakes:
            total += cake.price

        if not change:

            if total + obj.price > 10000:
                return

            # Пекар не може да додаде торта, ако веќе постои торта со истото име.
            if Cake.objects.filter(name = obj.name).exists():
                return

        super().save_model(request, obj, form, change)

    # Тортите можат да бидат менувани само од пекарите кои ги додале, а останатите пекари може само да ги гледаат тие торти.
    def has_change_permission(self, request, obj = None):
        return obj and obj.baker.user == request.user


admin.site.register(Baker, BakerAdmin)
admin.site.register(Cake, CakeAdmin)

