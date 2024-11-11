from django.db import models
from apps.core.models import AbstractBaseModel


# Create your models here.


class Todo(AbstractBaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True)
    completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.title
