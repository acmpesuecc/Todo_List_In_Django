from django.db import models
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    # Todo create a title attribute -> char
    title = models.CharField(max_length=255)

    # Todo create a content attribute -> text
    content = models.CharField(max_length=1000)

    # Todo create a created_at attribute -> timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    # Todo create priority attribute -> integer
    priority = models.IntegerField(default=1)

    def __str__(self):
        # Todo return title
        return f"{self.title}"
