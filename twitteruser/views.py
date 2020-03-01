from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from twitteruser.forms import LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from tweet.models import Tweet

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='http://localhost:8000/login/')
def homepage(request):
    html = "home.html"

    user = TwitterUser.objects.get(username=request.user)
    # tweet = Tweet.objects.get(twittuser=request.user)

    followerCount = len(user.friend.all())
    # tweetCount = len(tweet)
    print("Does this work Count?")
    items = Tweet.objects.all().order_by('-date_filed')

    return render(request, html,
                  {
                    'items': items,
                    # 'tweetCount': tweetCount,
                    'followerCount': followerCount
                  })


def loginUser(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    form = LoginForm()

    return render(request, html, {'form': form})


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))


def signupUser(request):
    html = "signup.html"

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )

            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()

    return render(request, html, {"form": form})


def profileUser(request, profile):
    html = "profile.html"
    userTweets = Tweet.objects.filter(twittuser=request.user)

    return render(request, html,
                  {
                    'userTweets': userTweets,
                    'profile': profile
                  })


def followerView(request, name):
    a1 = TwitterUser.objects.get(username=name)
    p1 = TwitterUser.objects.get(username='bowser')

    a1.friend.add(p1)

    len(a1.friend.all())

    # a1.friend.remove(p1)

    return HttpResponseRedirect(reverse("homepage"))


def unfollowerView(request, name):
    b1 = TwitterUser.objects.get(username=name)
    q1 = TwitterUser.objects.get(username='bowser')

    # a1.friend.add(p1)

    # len(a1.friend.all())

    b1.friend.remove(q1)

    return HttpResponseRedirect(reverse("homepage"))