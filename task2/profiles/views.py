from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# from profiles.models import UserProfile
# from profiles.serializers import UserProfileSerializer
#
#
# class UserProfileViewSet(ModelViewSet):
#     queryset = UserProfile.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = UserProfileSerializer


# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email,
#             'password': user.password
#         })
