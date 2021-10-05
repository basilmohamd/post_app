from django.db import models
import datetime


# Create your models here.
from django.db.models import IntegerField


class Task(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField(null=True,blank=True)
    date = models.DateField(default=datetime.date.today)
