from rest_framework import serializers

from question.models import Rate
from profiles.models import UserProfile, Tag


class UserProfileSerializer(serializers.ModelSerializer):
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'avatar', 'place_of_employment', 'about_yourself', 'location', 'RANK_CHOICES',
                  'STATUS_CHOICES', 'user_rating']

    def get_user_rating(self, instance):
        arr = Rate.objects.filter(id=instance)
        res = 0
        for obj in arr:
            res += obj['count']
        return res


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'question_id']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'user_id', 'tag_id']
