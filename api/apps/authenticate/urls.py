from django.urls import path

from apps.authenticate.views import LoginViewSet, RefreshTokenViewSet

urlpatterns = [
    # JWT Authentication
    path("token/", LoginViewSet.as_view(), name="token"),
    path("token/refresh/", RefreshTokenViewSet.as_view(), name="refresh_token"),
]
