from rest_framework import serializers

from question.models import Question, Answer, Comment, Rate, Tag, Skill


class QuestionSerializer(serializers.ModelSerializer):
    # question_rating = serializers.SerializerMethodField()

    class Meta:
        model = Question
        # fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id', 'question_rating']
        fields = '__all__'

    # def get_question_rating(self, instance):
    #     arr = Rate.objects.filter(id=instance)
    #     res = 0
    #     for obj in arr:
    #         res += obj['count']
    #         print('====================================================Res: ', res)
    #     return res


class AnswerSerializer(serializers.ModelSerializer):
    # answer_rating = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = '__all__'
#         fields = ['id', 'title', 'body', 'date_create', 'date_update', 'user_id', 'question_id', 'answer_rating']
#
#     def get_answer_rating(self, instance):
#         arr = Rate.objects.filter(id=instance)
#         res = 0
#         for obj in arr:
#             res += obj['count']
#         return res


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
