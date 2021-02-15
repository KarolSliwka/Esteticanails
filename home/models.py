from django.db import models


class Logotype(models.Model):
    """ Main page logotype """
    class Meta:
        verbose_name_plural = "Logotype"

    name = models.CharField(max_length=150, null=True, default='logotype')
    image = models.ImageField(upload_to="logotype/", null=True, blank=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    """ Footer social media icons """
    class Meta:
        verbose_name_plural = "Social Media's"

    Social_Choices = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('Pinterest', 'Pinterest'),
        ('Snapchat', 'Snapchat'),
        ('TikTok', 'TikTok'),
        ('Twitter', 'Twitter'),
        ('WhatsApp', 'WhatsApp'),
        ('YouTube', 'YouTube'),
    ]

    name = models.CharField(max_length=150, null=True,
                            blank=False, choices=Social_Choices)
    url = models.URLField(
        max_length=1024, default='', null=True, blank=True)

    def __str__(self):
        return self.name


class Slides(models.Model):
    """ """
    class Meta:
        verbose_name_plural = "Slides"

    name = models.CharField(max_length=50, default='Slide ', editable=False)
    image = models.ImageField(
        upload_to="images/carousel/", null=True, blank=True)
    title = models.CharField(max_length=124, null=True, blank=True)
    text = models.TextField(max_length=1024, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = 'Slide ' + str(Slides.objects.count() + 1)

        super(Slides, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
