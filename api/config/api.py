from django.urls import include, path

urlpatterns = [
    path("todo/", include("apps.todos.urls")),
    path("auth/", include("apps.authenticate.urls")),
]
