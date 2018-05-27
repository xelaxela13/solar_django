from django.views.generic import TemplateView
from project.seometa import MyMetadataMixin
from django.utils.translation import gettext_lazy as _


class Index(MyMetadataMixin, TemplateView):
    title = _('IceBERG')
    template_name = 'home/index.html'
