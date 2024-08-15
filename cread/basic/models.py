from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Home1(models.Model):
    name=models.TextField(max_length=100)
    passw=models.TextField(max_length=100)