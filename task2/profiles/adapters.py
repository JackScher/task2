from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class CustomAdapter(DefaultAccountAdapter):
    # def send_confirmation_mail(self, request, emailconfirmation, signup):
    #     current_site = get_current_site(request)
    #     activate_url = self.get_email_confirmation_url(request, emailconfirmation)
    #     # activate_url = 'http://127.0.0.1:8080/#/confirm/'
    #     ctx = {
    #         # "user": emailconfirmation.email_address.user,
    #         # "activate_url": activate_url,
    #         # "current_site": current_site,
    #         # "key": emailconfirmation.key,
    #
    #         "user": emailconfirmation.email_address.user,
    #         "activate_url": activate_url,
    #         "current_site": current_site,
    #         "key": emailconfirmation.key,
    #     }
    #     if signup:
    #         email_template = "account/email/email_confirmation_signup"
    #     else:
    #         email_template = "account/email/email_confirmation"
    #     self.send_mail(email_template, emailconfirmation.email_address.email, ctx)

    # def get_email_confirmation_url(self, request, emailconfirmation):
    #     """Constructs the email confirmation (activation) url.
    #
    #     Note that if you have architected your system such that email
    #     confirmations are sent outside of the request context `request`
    #     can be `None` here.
    #     """
    #     # url = reverse("account_confirm_email", args=[emailconfirmation.key])
    #     url = "confirm"
    #     # ret = build_absolute_uri(request, url)
    #     # return ret
    #     return settings.FRONTEND_HOST + url

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.FRONTEND_HOST + '/verify-email/' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
