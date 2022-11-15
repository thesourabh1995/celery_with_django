from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json;

# Create your views here.
def test(request):
    test_func.delay()  # type: ignore
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()  # type: ignore
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=13, minute=20)
    task = PeriodicTask.objects.create(crontab=schedule, task='send_mail_app.tasks.send_mail_func', name="schedule_mail_task_"+"12")
    return HttpResponse("Done")