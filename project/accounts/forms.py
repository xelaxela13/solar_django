from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'location', 'password1', 'password2', )
        widgets = {
            'location': forms.HiddenInput(),
        }
