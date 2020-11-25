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

from profiles.models import UserProfile, StatusChoice
from profiles.serializers import UserProfileSerializer, UpdateUserProfileSerializer, CustomRegisterSerializer


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


class RegisterUserProfileView(RegisterView):
    serializer_class = CustomRegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    # def status_mapping(self, status):
    #     status_mapping = {
    #         'none': StatusChoice.status1,
    #         'educating': StatusChoice.status2,
    #         'working': StatusChoice.status3
    #     }
    #     if status:
    #         return status_mapping.get(status, StatusChoice.status1)
    #     return StatusChoice.status1


class UpdateUserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UpdateUserProfileSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print(request.data)
        user = UserProfile.objects.get(id=request.data['id'])
        if request.data['username']:
            user.username = request.data['username']
            user.save()
        if user.about_yourself and request.data['about_yourself']:
            user.about_yourself = request.data['about_yourself']
            user.save()
        elif request.data['about_yourself'] and user.about_yourself==None:
            user.rating += 1
            user.about_yourself = request.data['about_yourself']
            user.save()

        if user.place_of_employment and request.data['place_of_employment']:
            user.place_of_employment = request.data['place_of_employment']
            user.save()
        elif request.data['place_of_employment'] and user.place_of_employment==None:
            user.rating += 1
            user.place_of_employment = request.data['place_of_employment']
            user.save()

        if user.location and request.data['location']:
            user.location = request.data['location']
            user.save()
        elif request.data['location'] and user.location==None:
            user.rating += 1
            user.location = request.data['location']
            user.save()

        return Response({'detail': ('ok')}, status=status.HTTP_200_OK)
