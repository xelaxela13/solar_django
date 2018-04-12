from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountsSignup.as_view(), name='signup')
]