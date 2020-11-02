from rest_framework import serializers

from task2.chatting.models import Question, Answer, Comment


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
