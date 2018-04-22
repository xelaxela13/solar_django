from django.conf import settings


def settings_to_template(request):
    ctx = {'SITE_LOGO_FIRST': settings.SITE_LOGO_FIRST,
           'SITE_LOGO_SECOND': settings.SITE_LOGO_SECOND}
    return ctx
