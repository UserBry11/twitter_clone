from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification

from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='http://localhost:8000/login/')
def homepage(request):
    html = "home.html"
# User .get() to return one single query object. Use .filter() for multiple
    baseUser = TwitterUser.objects.get(username=request.user)
    tweet_count = Tweet.objects.filter(twittuser__username=request.user).count()

    followerCount = len(baseUser.follower.all())

    tweets = Tweet.objects.filter(twittuser__in=request.user.follower.all()).order_by("-date_filed")

    notification = Notification.objects.filter(target_user=request.user).filter(seen=False)

    users_list = TwitterUser.objects.all()

    return render(request, html,
                  {
                    'items': tweets,
                    'tweetCount': tweet_count,
                    'followerCount': followerCount,
                    'notification_count': notification.count(),
                    'users_list': users_list,
                  })


def profileUser(request, profile):
    html = "profile.html"
    userTweets = Tweet.objects.filter(twittuser=request.user).order_by("-date_filed")

    exists = False
    target_user = TwitterUser.objects.filter(username=profile).first()
    # if TwitterUser.objects.filter(follower__in=[request.user, profile]).exists():
    if target_user in request.user.follower.all():
        exists = True

    return render(request, html,
                  {
                    'userTweets': userTweets,
                    'profile': profile,
                    'exists': exists
                  })


def followerView(request, name):
    ProfileA = TwitterUser.objects.get(username=request.user)
    NewFriend = TwitterUser.objects.get(username=name)

    ProfileA.follower.add(NewFriend)

    return HttpResponseRedirect(reverse("homepage"))


def unfollowerView(request, name):
    ProfileA = TwitterUser.objects.get(username=request.user)
    NotFriend = TwitterUser.objects.get(username=name)

    ProfileA.follower.remove(NotFriend)

    return HttpResponseRedirect(reverse("homepage"))
