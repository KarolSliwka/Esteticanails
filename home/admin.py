from django.contrib import admin
from .models import Logotype, SocialMedia, Slide


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


class AdminSlide(admin.ModelAdmin):
    """ """
    list_display = (
        'name',
        'image',
    )

    ordering = ('name',)


admin.site.register(Logotype, AdminLogotype)
admin.site.register(SocialMedia, AdminSocialMediaIcons)
admin.site.register(Slide, AdminSlide)
