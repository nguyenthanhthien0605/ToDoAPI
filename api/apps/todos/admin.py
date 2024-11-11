from django.contrib import admin

from apps.todos.models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
