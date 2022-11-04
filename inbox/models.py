from django.db import models
from datetime import datetime

class Mail(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name