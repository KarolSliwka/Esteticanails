from django.db import models


class ContactHeader(models.Model):
    class Meta:
        verbose_name_plural = "Contact Info"

    name = models.CharField(
        max_length=100, default='Contact Information', editable=False)
    title = models.CharField(max_length=128)
    promo_text = models.TextField(max_length=1024, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(
        upload_to="images/contact", null=True, blank=True)

    def __str__(self):
        return self.name
