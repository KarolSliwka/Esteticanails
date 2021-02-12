from django.contrib import admin
from .models import Logotype, SocialMedia


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


admin.site.register(Logotype, AdminLogotype)
admin.site.register(SocialMedia, AdminSocialMediaIcons)
