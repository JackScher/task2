from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_username, user_field
from django.conf import settings

from profiles.models import UserProfile


class CustomAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url.

        Note that if you have architected your system such that email
        confirmations are sent outside of the request context `request`
        can be `None` here.
        """
        url = settings.FRONTEND_HOST + '/?URLquery=' + emailconfirmation.key
        return url

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        user_email(user, email)
        user_username(user, username)
        status = data.get("status")
        place_of_employment = data.get("place_of_employment")
        about_yourself = data.get("about_yourself")
        location = data.get("location")
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if status:
            user_field(user, "status", status)
        if place_of_employment:
            user_field(user, "place_of_employment", place_of_employment)
        if about_yourself:
            user_field(user, "about_yourself", about_yourself)
        if location:
            user_field(user, "location", location)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
