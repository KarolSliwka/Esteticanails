from django.contrib import admin
from .models import GalleryImage


class AdminGalleryImage(admin.ModelAdmin):

    list_display = (
        'name',
        'image',
    )

    ordering = ('name',)


admin.site.register(GalleryImage, AdminGalleryImage)
