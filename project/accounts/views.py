from .forms import SignUpForm
import requests
from django.views.generic.edit import CreateView


def get_location(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/{}'.format(ip_address), timeout=5, verify=False)
    geodata = response.json()
    try:
        city = geodata['city']
    except KeyError:
        return None
    return city


class AccountsSignup(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def get_initial(self):
        initial = super(AccountsSignup, self).get_initial()
        initial['location'] = get_location(self.request)
        return initial

    def get_form(self, form_class=None):
        form = super(AccountsSignup, self).get_form(form_class)
        form.fields['phone'].required = True
        return form



