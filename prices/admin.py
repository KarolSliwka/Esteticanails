from django.contrib import admin
from .models import ServiceCategory, Service


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'offer',
        'offer_price',
    )

    ordering = ('name',)


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service, ServiceAdmin)
