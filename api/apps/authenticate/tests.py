import logging

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class AuthenticateAPITestCase(TestCase):
    url = "/v1/auth"

    def setUp(self):
        user = User.objects.create_superuser(username="admin", password="admin")
        self.client = APIClient()

    def test_get_access_token(self):
        response = self.client.post(
            path=f"{self.url}/token/",
            data={
                "username": "admin",
                "password": "admin",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_access_token_wrong_username_or_password(self):
        response = self.client.post(
            path=f"{self.url}/token/",
            data={
                "username": "admin123",
                "password": "admin",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_refresh_token(self):
        token = self.client.post(
            path=f"{self.url}/token/",
            data={
                "username": "admin",
                "password": "admin",
            },
        ).json()

        response = self.client.post(
            path=f"{self.url}/token/refresh/",
            data={
                "refresh": token.get("refresh"),
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
