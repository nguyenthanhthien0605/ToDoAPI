from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from dj_rest_auth.views import LoginView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authenticate.serializers import (
    ResponseTokenSerializer,
    UserLoginBodySerializer,
)
from drf_yasg import openapi


class LoginViewSet(LoginView):
    def get_response(self):
        serializer_class = TokenObtainPairSerializer()
        serializer = serializer_class.get_token(self.user)
        access = serializer.access_token
        data = {
            "refresh": str(serializer),
            "access": str(access),
        }
        return Response(
            data=ResponseTokenSerializer(data).data, status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        request_body=UserLoginBodySerializer,
        responses={
            200: openapi.Response("Response Description", ResponseTokenSerializer)
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RefreshTokenViewSet(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response("Response Description", ResponseTokenSerializer)
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
