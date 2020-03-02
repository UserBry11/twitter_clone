from django.shortcuts import render, reverse, HttpResponseRedirect
from notification.models import Notification
# Create your views here.


def notification_view(request):
    html = "notification.html"

    notifications = Notification.objects.filter(target_user=request.user).filter(seen=False).all().order_by('-date_filed')
    notification_count = notifications.count()
    return render(request, html,
                  {
                      "notifications": notifications,
                      "notify_count": notification_count
                  })


def cleared_notifications(request):
    notifications = Notification.objects.filter(target_user=request.user).all()

    for each in notifications:
        each.seen = True
        each.save()

    return HttpResponseRedirect(reverse("notifications"))
