from django.db import models
from datetime import datetime


class Education(models.Model):
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=500)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.school


    def year(self):
        return self.start_date.strftime("%b %Y") + "-" + self.end_date.strftime("%b %Y")