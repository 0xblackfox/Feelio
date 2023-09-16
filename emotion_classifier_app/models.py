from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Song(models.Model):
    emotion = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    link = models.URLField()  # Add the link field
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.emotion

