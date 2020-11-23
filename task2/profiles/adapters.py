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
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
###########################################################
        about_yourself = request.data.get("about_yourself")
        place_of_employment = request.data.get("place_of_employment")
        location = request.data.get("location")
        # status = request.data.get("STATUS_CHOICES")
###########################################################
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if "password1" in data:
            user.set_password(data["password1"])

###########################################################

        if about_yourself:
            user.about_yourself = about_yourself
            user.save()
        if place_of_employment:
            user.place_of_employment = place_of_employment
            user.save()
        if location:
            user.location = location
            user.save()

        # if status:
        #     # print('IN STATUS: ', user.STATUS_CHOICES)
        #     # user.STATUS_CHOICES = status
        #     # print(user.STATUS_CHOICES)
        #     # user.save()
        #     for status_c in user.STATUS_CHOICES[0]:
        #         if status == status_c[1]:
        #             user.STATUS_CHOICES = status_c
        #             user.save()



###########################################################

        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
