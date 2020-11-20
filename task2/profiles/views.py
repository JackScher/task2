from allauth.account.views import ConfirmEmailView
from django_filters.rest_framework import DjangoFilterBackend
# from rest_auth.models import TokenModel
# from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
# from rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer, CreateUserProfileSerializer


class CustomView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['token', 'id']

    def post(self, request, key, *args, **kwargs):
        # print(request)
        confirmation = self.get_object()
        confirmation.confirm(key)
        return Response({'detail': ('ok')}, status=status.HTTP_200_OK)


class ProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']
    serializer_class = UserProfileSerializer


class UpdateUserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = CreateUserProfileSerializer


# class RegisterUserProfileView(APIView, RegisterView):
#     permission_classes = (AllowAny,)
#     allowed_methods = ('POST', 'OPTIONS', 'HEAD')
#
#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         print('serializer: ', serializer)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_create(serializer)
#         print('user: ', user)
#         headers = self.get_success_headers(serializer.data)
#
#         return Response(self.get_response_data(user),
#                         status=status.HTTP_201_CREATED,
#                         headers=headers)
