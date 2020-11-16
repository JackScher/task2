from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
#
# from question.models import Rate
# from rest_framework.authtoken.models import Token

from profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    # user_rating = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar', 'place_of_employment', 'about_yourself', 'location',
                  'RANK_CHOICES', 'STATUS_CHOICES']
        # extra_kwargs = {'password': {'required': True, 'write_only': True}}

    # def create(self, validated_data):
    #     user = UserProfile.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user


#
#     def user_rating(self, instance):
#         arr = Rate.objects.filter(id=instance)
#         res = 0
#         for obj in arr:
#             res += obj['count']
#         return res
