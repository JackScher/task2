from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from question.models import Question, Answer, Comment, Rate, Tag, Skill
from question.serializers import QuestionSerializer, AnswerSerializer, CommentSerializer, RateSerializer, TagSerializer, \
    SkillSerializer, QuestionItemSerializer, QuestionCreateSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = QuestionSerializer


class QuestionItemViewSet(ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    serializer_class = QuestionItemSerializer


class QuestionCreateView(ModelViewSet):
    queryset = Question.objects.all()
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = QuestionCreateSerializer


####################################################################


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user_id', 'id', 'question_id']
    serializer_class = AnswerSerializer


# class AnswerItemViewSet(ModelViewSet):
#     queryset = Answer.objects.all()
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#     filter_backends = [DjangoFilterBackend]
#     filter_fields = ['id']
#     serializer_class = AnswerItemSerializer


####################################################################


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
