from django.db import models

# Create your models here.
class TodoModel(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()