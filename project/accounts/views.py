from django.views.generic import TemplateView, ListView
from .forms import SignUpForm
import requests
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from project.seometa import MetadataMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_location(request):
    ip_address = get_client_ip(request)
    response = requests.get('http://api.ipstack.com/{}'.format(ip_address), timeout=5, verify=False,
                            params={'access_key': settings.IPSTACK_ACCESS_KEY, 'language': 'ru'})
    geodata = response.json()
    try:
        city = geodata['city']
    except KeyError:
        return ''
    return city


class AccountsSignup(SuccessMessageMixin, CreateView):
    template_name = 'accounts/registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = _('Registration was successful, please log in')

    def get_initial(self):
        initial = super(AccountsSignup, self).get_initial()
        city = get_location(self.request)
        initial['location'] = city
        messages.info(self.request, '{}'.format(city))
        return initial

    def get_form(self, form_class=None):
        form = super(AccountsSignup, self).get_form(form_class)
        form.fields['phone'].required = True
        return form


class AccountsPanel(SuccessMessageMixin, MetadataMixin, TemplateView):
    title = _('Control panel')
    description = _('My description')
    template_name = 'accounts/panel/panel.html'

    def get(self, request, *args, **kwargs):
        messages.success(request, '{} {}'.format(_('Welcome'), request.user.first_name))
        return super(AccountsPanel, self).get(request, *args, **kwargs)


class AccountsUpdate(SuccessMessageMixin, MetadataMixin, UpdateView):
    title = _('Update account')
    model = User
    template_name = 'accounts/panel/update.html'
    fields = ['first_name', 'last_name', 'email', 'phone', 'location']
    success_url = reverse_lazy('panel')
    success_message = _('Updated success!')


@method_decorator(staff_member_required, name='dispatch')
class AccountsUsersList(SuccessMessageMixin, MetadataMixin, ListView):
    title = _('A list of users')
    model = User
    template_name = 'accounts/panel/users_list.html'

