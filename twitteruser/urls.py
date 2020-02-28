from django.urls import path
from twitteruser import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),
    path('signup/', views.signupUser),
]
