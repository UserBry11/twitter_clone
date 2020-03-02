from django.db import models
from django.contrib.auth.models import AbstractUser
# from tweet.models import Tweet


# Create your models here.
class TwitterUser(AbstractUser):
    follower = models.ManyToManyField("self", blank=True, symmetrical=False)
