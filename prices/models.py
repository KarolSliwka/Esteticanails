from django.db import models


class ServiceCategory(models.Model):
    """ Service categories """
    class Meta:
        verbose_name_plural = 'Service Categories'

    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.friendly_name


class Service(models.Model):
    """ """
    offer_choices = ((True, 'Yes'), (False, 'No'))

    """ """
    name = models.CharField(max_length=254, null=False, blank=False)
    category = models.ForeignKey(
        'ServiceCategory', null=True, blank=False, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    time = models.TimeField(default="00:00:00")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=False)
    offer = models.BooleanField(choices=offer_choices)
    offer_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=False)

    def __str__(self):
        return self.name
