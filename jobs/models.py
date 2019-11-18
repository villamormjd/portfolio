from django.db import models
from datetime import datetime


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    resign_date = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return self.title

    def year(self):
        return self.hire_date.strftime("%b %Y")


    def resign_year(self):
        return self.resign_date.strftime("%b %Y")

    def diff_month(self):
        if not self.resign_date:
            self.resign_date = datetime.now()

        return (self.resign_date.year - self.hire_date.year) * 12 + self.resign_date.month - self.hire_date.month

    def desc_format(self):

        return self.description.split(".")