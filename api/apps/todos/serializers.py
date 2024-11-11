from rest_framework import serializers
from apps.todos.models import Todo


class ReadTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, attrs):
        return super().create(attrs)


class UpdateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def update(self, instance, attrs):
        return super().update(instance, attrs)
