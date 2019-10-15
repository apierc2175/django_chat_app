from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

class Topic(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chats:index')
