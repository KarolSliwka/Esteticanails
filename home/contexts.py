from datetime import datetime
from .models import SocialMedia


def FooterContext(context):

    social_media = SocialMedia.objects.all().order_by('name')
    currentYear = datetime.now().year

    if social_media.count() != 0:
        context = {
            'social_media': social_media,
            'currentYear': currentYear,
        }
    else:
        context = {
            'currentYear': currentYear,
        }

    return context
