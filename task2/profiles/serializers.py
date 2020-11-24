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
    # class Meta:
    #     model = UserProfile
    #     fields = ('place_of_employment', 'about_yourself', 'location', 'status')

    status = serializers.CharField()
    rank = serializers.CharField()

    place_of_employment = serializers.CharField()
    about_yourself = serializers.CharField()
    location = serializers.CharField()
    rating = serializers.IntegerField()

    def get_cleaned_data(self):
        return {
            'status': self.validated_data.get('status', ''),
            'rank': self.validated_data.get('rank', ''),
            'place_of_employment': self.validated_data.get('place_of_employment', ''),
            'about_yourself': self.validated_data.get('about_yourself', ''),
            'location': self.validated_data.get('location', ''),
            # 'rating': self.validated_data.get('rating', ''),
        }



class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'status', 'rank']
