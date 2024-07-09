from django.db import models
from django.contrib.auth.models import User

class Information(models.Model):

    user        = models.ForeignKey(User,related_name='information',on_delete=models.CASCADE )
    phone       = models.CharField(max_length=14)
    division    = models.CharField(max_length=20)
    district    = models.CharField(max_length=20)
    gender      = models.CharField(max_length=10)
