from django.db import models


class GalleryImage(models.Model):
    """ """
    class Meta:
        verbose_name_plural = "Gallery Images"

    name = models.CharField(max_length=50, default='Image', editable=False)
    image = models.ImageField(
        upload_to="images/gallery/", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = 'Image ' + str(GalleryImage.objects.count() + 1)

        super(GalleryImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
