from django.contrib import admin
from .models import SocialMediaIcon


class AdminSocialMediaIcons(admin.ModelAdmin):
    """  """
    list_display = (
        'name',
        'social_url',
    )

    ordering = ('name',)


admin.site.register(SocialMediaIcon, AdminSocialMediaIcons)
