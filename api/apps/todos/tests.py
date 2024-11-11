from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class TodoAPICreateTestCase(TestCase):
    url = "/v1/todo"
    url_login = "/v1/auth/token/"

    def setUp(self):
        user = User.objects.create_superuser(username="admin", password="admin")
        self.client = APIClient()

        # Get and set token from temporary user
        response_login = self.client.post(
            path=self.url_login, data={"username": "admin", "password": "admin"}
        )

        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + response_login.data.get("access")
        )

    def test_create_todo(self):
        response = self.client.post(
            path=f"{self.url}/",
            data={
                "title": "Test Todo",
                "description": "Test description",
                "completed": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_todo_missing_value_title(self):
        response = self.client.post(
            path=f"{self.url}/",
            data={
                "description": "Test description",
                "completed": False,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TodoAPIRetrieveUpdateDestroyTestCase(TodoAPICreateTestCase):
    def setUp(self):
        super().setUp()
        self.todo = self.client.post(
            path=f"{self.url}/",
            data={
                "title": "Test Todo",
                "description": "Test description",
                "completed": False,
            },
        ).json()

    def test_retrieve_todo(self):
        response = self.client.get(path=f"{self.url}/{self.todo.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_error_todo(self):
        response = self.client.get(path=f"{self.url}/123/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_todo(self):
        response = self.client.patch(
            path=f"{self.url}/{self.todo.get('id')}/",
            data={
                "title": "Test Update Title",
                "description": "Test Update Description",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo_title_blank(self):
        response = self.client.patch(
            path=f"{self.url}/{self.todo.get('id')}/",
            data={
                "title": "",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_todo(self):
        response = self.client.delete(path=f"{self.url}/{self.todo.get('id')}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
