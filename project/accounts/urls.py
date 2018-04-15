from django.urls import path
from .views import AccountsSignup, AccountsPanel, AccountsUpdate
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('signup/', AccountsSignup.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(template_name='accounts/registration/login.html'), name='login'),
    path('panel/', login_required(AccountsPanel.as_view()), name='panel'),
    path('panel/<int:pk>', AccountsUpdate.as_view(), name='user_update'),

    # standard django.contrib.auth templates
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
