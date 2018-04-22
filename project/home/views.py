from django.views.generic import TemplateView
from project.seometa import MetadataMixin
from django.utils.translation import gettext_lazy as _


class Index(MetadataMixin, TemplateView):
    title = _('IceBERG solar systems company')
    template_name = 'home/index.html'

