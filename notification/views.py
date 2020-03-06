from django.shortcuts import render, reverse, HttpResponseRedirect
from notification.models import Notification
from django.views import View


class NotificationsView(View):
    def get(self, request):
        html = "notification.html"

        notifications = Notification.objects.filter(target_user=request.user).filter(seen=False).all().order_by('-date_filed')
        notification_count = notifications.count()
        return render(request, html,
                      {
                        "notifications": notifications,
                        "notify_count": notification_count
                      })


class ClearNotification(View):
    def get(request):
        notifications = Notification.objects.filter(target_user=request.user).all()

        for each in notifications:
            each.seen = True
            each.save()

        return HttpResponseRedirect(reverse("notifications"))
