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
    # user_rating = serializers.SerializerMethodField()
    answers = AnswerModuleSerializer(many=True)
    questions = QuestionsModuleSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'RANK_CHOICES', 'STATUS_CHOICES', 'answers', 'questions', 'rating']
        # extra_kwargs = {'password': {'required': True, 'write_only': True}}

    # def create(self, validated_data):
    #     user = UserProfile.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user


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

#     def user_rating(self, instance):
#         arr = Rate.objects.filter(id=instance)
#         res = 0
#         for obj in arr:
#             res += obj['count']
#         return res


class CreateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'STATUS_CHOICES']
