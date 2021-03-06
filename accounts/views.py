from django.template.response import TemplateResponse
from django.views.generic import TemplateView, ListView
from .forms import SignUpForm
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.utils.translation import gettext_lazy as _
from project.seometa import MyMetadataMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .tasks import get_location


@csrf_exempt
def choice_location_manual(request):
    data = {'city': ''}
    if request.POST:
        try:
            data['city'] = request.POST['location']
        except KeyError:
            pass
        return JsonResponse(data=data)
    return TemplateResponse(request, 'accounts/choice_location_manual.html')


def choice_location_api(request):
    ip_address = [val for key, val in request.META.items() if key in ['HTTP_X_FORWARDED_FOR',
                                                                      'HTTP_X_REAL_IP',
                                                                      'REMOTE_ADDR']
                  ]
    city = get_location.apply_async(
        kwargs={'language_code': request.LANGUAGE_CODE, 'ip_address': ip_address[0]},
    )
    return JsonResponse(data={'city': city.result})


class AccountsLogin(SuccessMessageMixin, MyMetadataMixin, LoginView):
    template_name = 'accounts/registration/login.html'
    title = _('Log in')


class AccountsSignup(SuccessMessageMixin, MyMetadataMixin, CreateView):
    template_name = 'accounts/registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = _('Registration was successful, please log in')
    title = _('Sign up')

    def get_form(self, form_class=None):
        form = super(AccountsSignup, self).get_form(form_class)
        form.fields['phone'].required = True
        return form


class AccountsPanel(SuccessMessageMixin, MyMetadataMixin, TemplateView):
    title = _('Control panel')
    description = _('Control panel')
    template_name = 'accounts/panel/panel.html'

    def get(self, request, *args, **kwargs):
        messages.success(request, '{} {}'.format(_('Welcome'), request.user.first_name))
        return super(AccountsPanel, self).get(request, *args, **kwargs)


class AccountsUpdate(SuccessMessageMixin, MyMetadataMixin, UpdateView):
    title = _('Update account')
    model = User
    template_name = 'accounts/panel/update.html'
    fields = ['first_name', 'last_name', 'email', 'phone', 'location']
    success_url = reverse_lazy('panel')
    success_message = _('Updated success!')

    def get_initial(self):
        initial = super().get_initial()
        city = choice_location_api(self.request)
        if city:
            initial['location'] = city
        return initial


@method_decorator(staff_member_required, name='dispatch')
class AccountsUsersList(SuccessMessageMixin, MyMetadataMixin, ListView):
    title = _('A list of users')
    model = User
    template_name = 'accounts/panel/users_list.html'
