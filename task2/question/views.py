from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from question.models import Question, Answer, Comment, Rate, Tag, Skill
from question.serializers import QuestionSerializer, AnswerSerializer, CommentSerializer, RateSerializer, TagSerializer, \
    SkillSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user_id', 'id']
    serializer_class = QuestionSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = AnswerSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = CommentSerializer


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RateSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = SkillSerializer
