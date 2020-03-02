from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.loginUser),
    path('logout/', views.logoutUser),
    path('signup/', views.signupUser),
]
