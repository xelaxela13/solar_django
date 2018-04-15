from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True, verbose_name=_('City'))
    phone = models.CharField(max_length=15, blank=True, verbose_name=_('Phone number'),
                             help_text=_('Required field. Please enter your phone number'))

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_update', kwargs={'pk': self.pk})
