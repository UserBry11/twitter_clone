from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/<int:id>/', views.TweetView.as_view()),
    path('tweetform/', views.TweetFormView.as_view()),
]
