from django.db import models

# Create your models here.
class Sridhar(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    saddrs=models.CharField(max_length=50)