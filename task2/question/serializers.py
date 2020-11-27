from rest_framework import serializers

from profiles.models import UserProfile
from question.models import Question, Answer, Comment, Tag, Skill, Vote


class TagModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserProfileModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']


# class CommentCommentModuleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'text', 'content_type', 'object_id', 'user_id']


class CommentModuleSerializer(serializers.ModelSerializer):
    # object_id = CommentCommentModuleSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'text']


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
    user_id = UserProfileModuleSerializer()

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'answers', 'tags', 'comments', 'user_id']


#############################Question Item Serializser#############################


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id', 'question_id']

    # def create(self, validated_data):
    #     answer = Answer.objects.create(**validated_data)
    #     user = UserProfile.objects.get(id=answer.user_id.id)
    #     rating = Rating.objects.create()
    #     rating.answer_id.add(answer.id)
    #     rating.user_id.add(user.id)
    #     print('ANSWER ID: ', rating.answer_id)
    #     print('USER ID: ', rating.user_id)
    #     return answer


###################################################################################


class CommentCreateSerializer(serializers.ModelSerializer):
    # comment_rating = serializers.SerializerMethodField()
    # object_id = CommentCommentModuleSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'content_type', 'object_id', 'user_id']
        # fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'voter', 'action', 'date_create', 'date_update', 'content_type', 'object_id']


# class RateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rate
#         fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'question_id')


class TagUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'question_id')


class TagDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'question_id')


class RemoveTagRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'question_id')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
