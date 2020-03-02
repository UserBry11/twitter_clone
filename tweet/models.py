from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    tweetbody = models.CharField(max_length=140)
    date_filed = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30, default="")
    twittuser = models.ManyToManyField(TwitterUser, blank=True)

    def __str__(self):
        return self.tweetbody
