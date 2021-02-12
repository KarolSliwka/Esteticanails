from django.db import models


class SocialMedia(models.Model):
    """ Footer social media icons """
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
    social_url = models.URLField(
        max_length=1024, default='', null=True, blank=True)

    def __str__(self):
        return self.name
