from django.urls import path, include
from rest_auth.registration.views import VerifyEmailView
from rest_auth.registration.urls import TemplateView

from profiles.views import CustomView

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('confirmation/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # path('rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(), name='account_confirm_email'),
    path('registration/account-confirm-email/<str:key>', CustomView.as_view(), name='account_confirm_email'),
]