from rest_framework import serializers

from task2.core.models import UserProfile, Rate, Question, Answer, Comment, Tag


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


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id', 'question_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'date', 'user_id', 'content_object']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'question_id']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'user_id', 'tag_id']
