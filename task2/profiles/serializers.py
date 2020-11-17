from rest_framework import serializers
from rest_framework.authtoken.models import Token


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


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id']
        # fields = '__all__'


class MyCustomTokenSerializer(serializers.ModelSerializer):
    user = UserIdSerializer(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user')

#     def user_rating(self, instance):
#         arr = Rate.objects.filter(id=instance)
#         res = 0
#         for obj in arr:
#             res += obj['count']
#         return res
