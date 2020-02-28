from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    tweetbody = models.CharField(max_length=140)
    date_filed = models.DateTimeField(default=timezone.now)
    twittuser = models.ForeignKey(TwitterUser,
                                  blank=True,
                                  on_delete=models.CASCADE,
                                  default="",
                                  related_name="tweets")
