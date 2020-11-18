from rest_framework import serializers

from profiles.models import UserProfile
from question.models import Question, Answer, Comment, Rate, Tag, Skill


class TagModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserProfileModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']


class CommentModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class QuestionSerializer(serializers.ModelSerializer):
    tags = TagModuleSerializer(many=True)
    user_id = UserProfileModuleSerializer()
    comments = CommentModuleSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id', 'tags', 'comments']


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'user_id']


#############################Question List Serializser#############################


class AnswerModuleSerializer(serializers.ModelSerializer):
    user_id = UserProfileModuleSerializer()
    comments = CommentModuleSerializer(many=True)

    class Meta:
        model = Answer
        fields = ['id', 'title', 'body', 'user_id', 'comments']
        # fields = '__all__'


class QuestionItemSerializer(serializers.ModelSerializer):
    answers = AnswerModuleSerializer(many=True)
    tags = TagModuleSerializer(many=True)
    comments = CommentModuleSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'answers', 'tags', 'comments']


#############################Question Item Serializser#############################


class AnswerSerializer(serializers.ModelSerializer):
    user_id = UserProfileModuleSerializer()
    comments = CommentModuleSerializer(many=True)

    class Meta:
        model = Answer
        fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id', 'question_id', 'comments']


###################################################################################

#
# class AnswerItemSerializer(serializers.ModelSerializer):
#     user_id = UserProfileModuleSerializer()
#     comments = CommentModuleSerializer(many=True)
#
#     class Meta:
#         model = Answer
#         fields = ['id', 'title', 'body', 'user_id', 'comments']


##############################Answer Item Serializser##############################


class CommentSerializer(serializers.ModelSerializer):
    # comment_rating = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        # fields = ['id', 'date', 'user_id', 'content_object', 'comment_rating']
        fields = '__all__'

    # def get_comment_rating(self, instance):
    #     arr = Rate.objects.filter(id=instance)
    #     res = 0
    #     for obj in arr:
    #         res += obj['count']
    #     return res


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
