from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.todos.views import TodoViewSet

router = SimpleRouter()
router.register("", TodoViewSet, basename="todo")
urlpatterns = [path("", include(router.urls))]
