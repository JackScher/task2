from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from profiles.models import UserProfile
from question.models import Answer, Question


class AnswerModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title', 'body']


class QuestionsModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'body']


class UserProfileSerializer(serializers.ModelSerializer):
    answers = AnswerModuleSerializer(many=True)
    questions = QuestionsModuleSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'rank', 'status', 'answers', 'questions', 'rating']


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id']


class MyCustomTokenSerializer(serializers.ModelSerializer):
    user = UserIdSerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')


class CustomRegisterSerializer(RegisterSerializer):
    status = serializers.CharField(required=True, allow_blank=True)
    place_of_employment = serializers.CharField(required=True, allow_blank=True)
    about_yourself = serializers.CharField(required=True, allow_blank=True)
    location = serializers.CharField(required=True, allow_blank=True)

    # class Meta(RegisterSerializer.Meta):
    #     fields = ('status', 'place_of_employment', 'about_yourself', 'location')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'status': self.validated_data.get('status', ''),
            'place_of_employment': self.validated_data.get('place_of_employment', ''),
            'about_yourself': self.validated_data.get('about_yourself', ''),
            'location': self.validated_data.get('location', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.add_rating(user)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    def mapping_for_rating(self, user, field):
        rating_mapping = {
            'status': user.status,
            'place_of_employment': user.place_of_employment,
            'about_yourself': user.about_yourself,
            'location': user.location
        }
        if field:
            return rating_mapping.get(field, None)
        return None

    def add_rating(self, user):
        keys = user.__dict__.keys()
        for key in keys:
            res = self.mapping_for_rating(user, key)
            if res:
                user.rating += 1
        user.save()


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'status', 'rank']
