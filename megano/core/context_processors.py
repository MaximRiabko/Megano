from .models import SiteSettings

def load_settings(request):
    settings = {}
    for setting in SiteSettings.objects.all():
        if setting.is_boolean:
            settings[setting.name] = setting.value.lower() in ['true', 'yes', '1']
        else:
            settings[setting.name] = setting.value
    return {'site_settings': settings}