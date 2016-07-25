from django.contrib import admin

# Register your models here.
from email_logs.models import EmailLog

admin.site.register(EmailLog)