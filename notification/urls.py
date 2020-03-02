from django.urls import path
from notification import views

urlpatterns = [
    path('notification/', views.notification_view, name="notifications"),
    path('cleannotify/', views.cleared_notifications)
]
