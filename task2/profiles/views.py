from allauth.account.views import ConfirmEmailView
from django_filters.rest_framework import DjangoFilterBackend
# from rest_auth.models import TokenModel
# from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
# from rest_auth.registration.views import RegisterView
from rest_auth.models import TokenModel
from rest_auth.registration.app_settings import register_permission_classes, RegisterSerializer
from rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer, UpdateUserProfileSerializer


class CustomView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, key, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.confirm(key)
        return Response({'detail': ('ok')}, status=status.HTTP_200_OK)


class ProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    serializer_class = UserProfileSerializer


class UpdateUserRatingView(ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = UpdateUserProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = UserProfile.objects.get(id=request.data['id'])
        event = request.data.get("event")
        if event == 'plus':
            user.rating += 1
            user.save()
        if event == 'minus':
            user.rating -= 1
            user.save()
        return Response({'detail': ('ok')}, status=status.HTTP_200_OK)


class RegisterUserProfileView(RegisterView):
    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        if user.place_of_employment:
            user.rating += 1
            user.save()
        if user.about_yourself:
            user.rating += 1
            user.save()
        if user.location:
            user.rating += 1
            user.save()
        if user.STATUS_CHOICES:
            print(user.STATUS_CHOICES)
            user.rating += 1
            user.save()
        ###################################################
        # user.RANK_CHOICES = ('r1', 'Freshman'),
        # user.save()

        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)
