from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
    template_name = 'home/index.html'

    def dispatch(self, request, *args, **kwargs):
        return super(Index, self).dispatch(request, *args, **kwargs)
