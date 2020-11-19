from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from question.models import Question, Answer, Comment, Rate, Tag, Skill
from question.serializers import QuestionSerializer, RateSerializer, TagSerializer, \
    SkillSerializer, QuestionItemSerializer, QuestionCreateSerializer, AnswerCreateSerializer, CommentCreateSerializer


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
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = QuestionCreateSerializer


####################################################################


class AnswerCreateView(ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = AnswerCreateSerializer


####################################################################


class CommentViewSet(ModelViewSet):
    # allowed_methods = ('GET', 'PUT', 'POST', 'HEAD', 'OPTIONS')
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CommentCreateSerializer


####################################################################


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
