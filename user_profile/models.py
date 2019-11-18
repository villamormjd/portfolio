from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    github = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

