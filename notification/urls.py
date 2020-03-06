from django.urls import path
from notification import views

urlpatterns = [
    path('notification/', views.NotificationsView.as_view(), name="notifications"),
    path('cleannotify/', views.ClearNotification.as_view())
]
