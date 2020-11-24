from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from profiles.models import UserProfile
from question.models import Question, Answer, Comment, Tag, Skill, Vote
from question.serializers import QuestionSerializer, TagSerializer, \
    SkillSerializer, QuestionItemSerializer, QuestionCreateSerializer, AnswerCreateSerializer, CommentCreateSerializer, \
    VoteSerializer


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = UserProfile.objects.get(id=request.data['user_id'])
        user.rating += 1
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


####################################################################


class AnswerCreateView(ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = AnswerCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = UserProfile.objects.get(id=request.data['user_id'])
        user.rating += 1
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

####################################################################


class CommentViewSet(ModelViewSet):
    # allowed_methods = ('GET', 'PUT', 'POST', 'HEAD', 'OPTIONS')
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = CommentCreateSerializer


####################################################################

class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        # voter = UserProfile.objects.get(id=request.data['voter'])
        # if voter.rating > 50:
        #     try:
        #         is_voted = Vote.objects.get(voter=request.data['voter'], object_id=request.data['object_id'])
        #         if request.data['mode'] == 'plus' and is_voted.is_like:
        #             return Response({'detail': 'already liked'}, status=status.HTTP_200_OK)
        #         if request.data['mode'] == 'minus' and is_voted.is_dislike:
        #             return Response({'detail': 'already disliked'}, status=status.HTTP_200_OK)
        #         if request.data['mode'] == 'minus' and is_voted.is_like:
        #             user = UserProfile.objects.get(id=request.data['user_id'])
        #             user.rating -= 1
        #             user.save()
        #             is_voted.is_like = False
        #             is_voted.is_dislike = True
        #             is_voted.save()
        #             return Response({'detail': 'disliked'}, status=status.HTTP_200_OK)
        #         if request.data['mode'] == 'plus' and is_voted.is_dislike:
        #             user = UserProfile.objects.get(id=request.data['user_id'])
        #             user.rating += 1
        #             user.save()
        #             is_voted.is_dislike = False
        #             is_voted.is_like = True
        #             is_voted.save()
        #             return Response({'detail': 'liked'}, status=status.HTTP_200_OK)
        #     except:
        #         print('Created: ', request.data['create_data'])
        #         if request.data['mode'] == 'plus':
        #             user = UserProfile.objects.get(id=request.data['user_id'])
        #             user.rating += 1
        #             user.save()
        #             serializer = self.get_serializer(data=request.data)
        #             serializer.is_valid(raise_exception=True)
        #             res = self.perform_create(serializer)
        #             res.is_like = True
        #             res.save()
        #         if request.data['mode'] == 'minus':
        #             user = UserProfile.objects.get(id=request.data['user_id'])
        #             user.rating -= 1
        #             user.save()
        #             serializer = self.get_serializer(data=request.data)
        #             serializer.is_valid(raise_exception=True)
        #             res = self.perform_create(serializer)
        #             res.is_dislike = True
        #             res.save()
        #
        #         headers = self.get_success_headers(serializer.data)
        #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # else:
        #     return Response({'detail': 'low rating'}, status=status.HTTP_200_OK)
        try:
            is_voted = Vote.objects.get(voter=request.data['voter'], object_id=request.data['object_id'])
            if request.data['mode'] == 'plus' and is_voted.is_like:
                return Response({'detail': 'already liked'}, status=status.HTTP_200_OK)
            if request.data['mode'] == 'minus' and is_voted.is_dislike:
                return Response({'detail': 'already disliked'}, status=status.HTTP_200_OK)
            if request.data['mode'] == 'minus' and is_voted.is_like:
                user = UserProfile.objects.get(id=request.data['user_id'])
                user.rating -= 1
                user.save()
                is_voted.is_like = False
                is_voted.is_dislike = True
                is_voted.save()
                return Response({'detail': 'disliked'}, status=status.HTTP_200_OK)
            if request.data['mode'] == 'plus' and is_voted.is_dislike:
                user = UserProfile.objects.get(id=request.data['user_id'])
                user.rating += 1
                user.save()
                is_voted.is_dislike = False
                is_voted.is_like = True
                is_voted.save()
                return Response({'detail': 'liked'}, status=status.HTTP_200_OK)
        except:
            # print('Created: ', request.data)
            # question = Question.objects.get(id=request.data['object_id'])
            # now = datetime.now()
            # print(question.date_create, now)
            if request.data['mode'] == 'plus':
                user = UserProfile.objects.get(id=request.data['user_id'])
                user.rating += 1
                user.save()
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                res = self.perform_create(serializer)
                res.is_like = True
                res.save()
            if request.data['mode'] == 'minus':
                user = UserProfile.objects.get(id=request.data['user_id'])
                user.rating -= 1
                user.save()
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                res = self.perform_create(serializer)
                res.is_dislike = True
                res.save()

            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = SkillSerializer
