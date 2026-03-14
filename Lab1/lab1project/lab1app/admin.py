from django.contrib import admin

from .models import Category, Instructor, Training


# Register your models here.

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_name', 'instructor', 'short_description', 'category', 'user', 'image', 'price_per_training_session', 'number_of_available_spots')
    exclude = ["user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Instructor)
admin.site.register(Training, TrainingAdmin)
