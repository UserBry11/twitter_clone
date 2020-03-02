from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('profile/<slug:profile>/', views.profileUser),
    path('follow/<slug:name>/', views.followerView),
    path('unfollow/<slug:name>/', views.unfollowerView),
]
