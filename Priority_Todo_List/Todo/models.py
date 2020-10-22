from django.db import models
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    # Todo create a title attribute -> char
    title = ''

    # Todo create a content attribute -> text
    content = ''

    # Todo create a created_at attribute -> timestamp
    created_at = ''

    # Todo create priority attribute -> integer
    priority = ''

    def __str__(self):
        # Todo return title
        return ''
