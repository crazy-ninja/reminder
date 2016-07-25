from django.db import models


# Create your models here.
class RemindMe(models.Model):
    email = models.CharField(max_length=156, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        var = self.email if self.email else self.mobile
        return var + ', ' + str(self.date) + ', ' + str(self.time)
