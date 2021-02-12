from datetime import datetime
from .models import SocialMedia


def FooterContext():

    social_media = SocialMedia.objects.all().order_by('name')
    currentYear = datetime.now().year

    context = {
        'social_media': social_media,
        'currentYear': currentYear,
    }

    return context
