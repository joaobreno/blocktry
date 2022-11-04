from django.db import models
from datetime import datetime
from distutils.command.upload import upload
# Create your models here.

class Contract(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_contract = models.DateTimeField(default=datetime.now,blank=True)
    photo = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    cpf = models.CharField(max_length=11)
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    date_born = models.DateTimeField(default=datetime.now)
    phone = models.CharField(max_length=11)
    cep_number = models.CharField(max_length=8)



    def __str__(self):
        return self.name
