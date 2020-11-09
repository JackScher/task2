from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url.

        Note that if you have architected your system such that email
        confirmations are sent outside of the request context `request`
        can be `None` here.
        """
        url = settings.FRONTEND_HOST + '/?URLquery=' + emailconfirmation.key
        return url
