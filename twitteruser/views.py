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
    items = Tweet.objects.all()

    return render(request, html, {'items': items})


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
