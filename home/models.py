from django.db import models


class SocialMediaIcon(models.Model):
    """ Footer social media icons """
    name = models.CharField(max_length=150, null=True, blank=False)
    social_url = models.URLField(
        max_length=1024, default='', null=True, blank=True)

    def __str__(self):
        return self.name
