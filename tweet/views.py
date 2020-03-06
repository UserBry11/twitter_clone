from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from tweet.forms import TweetForm
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.views import View
import re


class TweetFormView(View):
    html = "tweetform.html"

    def get(self, request):
        form = TweetForm()
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = TweetForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            newTweet = Tweet(
                tweetbody=data['tweetbody'],
                date_filed=data['date_filed'],
                author=request.user
            )
            newTweet.save()
            # This newTweet['tweetbody'] is reaching into db
            # if '@' in newTweet['tweetbody']:
            pattern = re.search("@[\w\d]+", newTweet.tweetbody)

            if pattern is not None:
                pattern = pattern.group(0)[1:]
                target_user = TwitterUser.objects.get(username=pattern)

                Notification.objects.create(
                    target_user=target_user,
                    tweet=newTweet,
                )

                baseProfile = TwitterUser.objects.get(username=request.user)
                newTweet.twittuser.add(baseProfile)

            return HttpResponseRedirect(reverse("homepage"))

        return render(request, self.html, {"form": form})


class TweetView(View):
    def get(self, request, id):
        item = Tweet.objects.get(id=id)

        return render(request, 'tweetdetail.html', {'item': item})
