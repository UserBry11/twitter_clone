from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from tweet.forms import TweetForm


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


def tweetform_view(request):
    html = "tweetform.html"

    if request.method == "POST":
        form = TweetForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                tweetbody=data['tweetbody'],
                date_filed=data['date_filed'],
                twittuser=request.user
            )

            return HttpResponseRedirect(reverse("homepage"))

    form = TweetForm()

    return render(request, html, {"form": form})


def tweet(request, id):
    item = Tweet.objects.get(id=id)

    return render(request, 'tweetdetail.html', {'item': item})
