from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)