from datetime import datetime, timedelta
# import datetime

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
        voter = UserProfile.objects.get(id=request.data['voter'])
        if voter.rating > 50:
            try:
                is_voted = Vote.objects.get(voter=request.data['voter'], object_id=request.data['object_id'])
                if request.data['mode'] == 'plus' and is_voted.is_like:
                    return Response({'detail': 'already liked'}, status=status.HTTP_200_OK)
                if request.data['mode'] == 'minus' and is_voted.is_dislike:
                    return Response({'detail': 'already disliked'}, status=status.HTTP_200_OK)
                if request.data['mode'] == 'minus' and is_voted.is_like:
                    cant_vote = self.check_revote(is_voted)
                    if cant_vote:
                        return cant_vote
                    user = UserProfile.objects.get(id=request.data['user_id'])
                    user.rating -= 1
                    user.save()
                    is_voted.is_like = False
                    is_voted.is_dislike = True
                    is_voted.save()
                    return Response({'detail': 'disliked'}, status=status.HTTP_200_OK)
                if request.data['mode'] == 'plus' and is_voted.is_dislike:
                    cant_vote = self.check_revote(is_voted)
                    if cant_vote:
                        return cant_vote
                    user = UserProfile.objects.get(id=request.data['user_id'])
                    user.rating += 1
                    user.save()
                    is_voted.is_dislike = False
                    is_voted.is_like = True
                    is_voted.save()
                    return Response({'detail': 'liked'}, status=status.HTTP_200_OK)
            except:
                cant_vote = self.check_create_time(request)
                if cant_vote:
                    return cant_vote
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
        else:
            return Response({'detail': 'low rating'}, status=status.HTTP_200_OK)
        # try:
        #     is_voted = Vote.objects.get(voter=request.data['voter'], object_id=request.data['object_id'])
        #     if request.data['mode'] == 'plus' and is_voted.is_like:
        #         return Response({'detail': 'already liked'}, status=status.HTTP_200_OK)
        #     if request.data['mode'] == 'minus' and is_voted.is_dislike:
        #         return Response({'detail': 'already disliked'}, status=status.HTTP_200_OK)
        #     if request.data['mode'] == 'minus' and is_voted.is_like:
        #         cant_vote = self.check_revote(is_voted)
        #         if cant_vote:
        #             return cant_vote
        #         user = UserProfile.objects.get(id=request.data['user_id'])
        #         user.rating -= 1
        #         user.save()
        #         is_voted.is_like = False
        #         is_voted.is_dislike = True
        #         is_voted.save()
        #         return Response({'detail': 'disliked'}, status=status.HTTP_200_OK)
        #     if request.data['mode'] == 'plus' and is_voted.is_dislike:
        #         cant_vote = self.check_revote(is_voted)
        #         if cant_vote:
        #             return cant_vote
        #         user = UserProfile.objects.get(id=request.data['user_id'])
        #         user.rating += 1
        #         user.save()
        #         is_voted.is_dislike = False
        #         is_voted.is_like = True
        #         is_voted.save()
        #         return Response({'detail': 'liked'}, status=status.HTTP_200_OK)
        # except:
        #     cant_vote = self.check_create_time(request)
        #     if cant_vote:
        #         return cant_vote
        #
        #     if request.data['mode'] == 'plus':
        #         user = UserProfile.objects.get(id=request.data['user_id'])
        #         user.rating += 1
        #         user.save()
        #         serializer = self.get_serializer(data=request.data)
        #         serializer.is_valid(raise_exception=True)
        #         res = self.perform_create(serializer)
        #         res.is_like = True
        #         res.save()
        #
        #     if request.data['mode'] == 'minus':
        #         user = UserProfile.objects.get(id=request.data['user_id'])
        #         user.rating -= 1
        #         user.save()
        #         serializer = self.get_serializer(data=request.data)
        #         serializer.is_valid(raise_exception=True)
        #         res = self.perform_create(serializer)
        #         res.is_dislike = True
        #         res.save()
        #
        #     headers = self.get_success_headers(serializer.data)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def check_create_time(self, request):
        q_create = Question.objects.get(id=request.data['object_id'])
        date, date_now = self.convert(q_create)
        difference = date_now-date
        delta = timedelta(days=30)
        return self.return_result(difference, delta)

    def check_revote(self, voted):
        date, date_now = self.convert(voted)
        difference = date_now - date
        delta = timedelta(hours=3)
        return self.return_result(difference, delta)

    def convert(self, item):
        date = datetime.strptime(item.date_create.strftime("%b %d %Y %H:%M:%S"), "%b %d %Y %H:%M:%S")
        now = datetime.strptime(datetime.now().strftime("%b %d %Y %H:%M:%S"), "%b %d %Y %H:%M:%S")
        return date, now

    def return_result(self, difference, delta):
        if difference > delta:
            return Response({'detail': 'can`t vote'}, status=status.HTTP_200_OK)
        return None


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = TagSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = SkillSerializer
