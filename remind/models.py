from django.db import models


# Create your models here.
class RemindMe(models.Model):
    email = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    message = models.CharField(max_length=1000, null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        var = self.email if self.email else self.mobile
        return var
