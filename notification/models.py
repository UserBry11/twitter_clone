from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser
from tweet.models import Tweet
# Create your models here.


class Notification(models.Model):
    target_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    date_filed = models.DateTimeField(default=timezone.now)

    # / notification for persons
    # // who created notification
    # / if notifcatoin has been seen
