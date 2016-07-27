from django.utils import timezone
from email_logs.views import send_remind_mail
from remind.models import RemindMe
from reminder.celery import app


@app.task()
def notify_user():
    """
        Send Email to Remind the user if email is given
    :return:
    """
    current_time = timezone.now()
    reminders = RemindMe.objects.filter(email__isnull=False)
    for reminder in reminders:
        # To match the RemindMe object time with current time
        if reminder.date_time.date() == current_time.date() and reminder.date_time.hour == current_time.hour\
                and reminder.date_time.minute == current_time.minute:
            email_context = {
                'message': reminder.message,
            }
            recipient = [reminder.email]
            # Shoot the email to the given EmailID
            send_remind_mail(
                'extra/reminder_email.html', email_context,
                'extra/remind_subject.txt', recipient)