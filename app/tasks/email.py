from celery import shared_task
from django.core.mail import send_mail


@shared_task(name="send_email_job")
def send_email_job(subject, message, sender, receivers):
    print("send email job ", message)
    # send_mail(subject, message, sender, receivers)
