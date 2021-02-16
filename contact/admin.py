from django.contrib import admin
from .models import ContactHeader


class ContactHeaderAdmin(admin.ModelAdmin):
    """  """
    list_display = (
        'name',
        'title',
        'promo_text',
        'phone_number',
        'image',
    )

    ordering = ('name',)


admin.site.register(ContactHeader, ContactHeaderAdmin)
