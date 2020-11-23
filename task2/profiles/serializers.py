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
                  'RANK_CHOICES', 'STATUS_CHOICES', 'answers', 'questions', 'rating']


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id']
        # fields = '__all__'


class MyCustomTokenSerializer(serializers.ModelSerializer):
    user = UserIdSerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'STATUS_CHOICES']


# # class CustomRegisterSerializer(RegisterSerializer):
# #     def get_cleaned_data(self):
# #         print('it`s get cleaned data in adapter!')
# #         username = self.validated_data.get('username', '')
# #         print('validated_data.get(about_yourself): ', username)
# #         return {
# #             'username': self.validated_data.get('username', ''),
# #             'password1': self.validated_data.get('password1', ''),
# #             'email': self.validated_data.get('email', ''),
# #             'about_yourself': self.validated_data.get('about_yourself', ''),
# #             'location': self.validated_data.get('location', ''),
# #             'place_of_employment': self.validated_data.get('place_of_employment', '')
# #         }
