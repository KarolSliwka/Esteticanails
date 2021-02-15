from django.contrib import admin
from .models import Logotype, SocialMedia, Slides


class AdminLogotype(admin.ModelAdmin):
    """  """
    list_display = (
        'name',
        'image',
    )

    ordering = ('name',)


class AdminSocialMediaIcons(admin.ModelAdmin):
    """  """
    list_display = (
        'name',
        'url',
    )

    ordering = ('name',)


class AdminSlides(admin.ModelAdmin):
    """ """
    list_display = (
        'name',
        'image',
    )

    ordering = ('name',)


admin.site.register(Logotype, AdminLogotype)
admin.site.register(SocialMedia, AdminSocialMediaIcons)
admin.site.register(Slides, AdminSlides)
