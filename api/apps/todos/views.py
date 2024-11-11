from rest_framework.permissions import IsAuthenticated

from apps.core.views import BaseViewSet
from apps.todos.serializers import (
    ReadTodoSerializer,
    CreateTodoSerializer,
    UpdateTodoSerializer,
)
from apps.todos.models import Todo


class TodoViewSet(BaseViewSet):
    read_serializer_class = ReadTodoSerializer
    detail_serializer_class = ReadTodoSerializer
    create_serializer_class = CreateTodoSerializer
    update_serializer_class = UpdateTodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
