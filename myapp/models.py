from django.db import models
from django.db import migrations, models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
 

# Create your models here.
class Client(models.Model):
        USERNAME=models.CharField(max_length=50,null=True)
        PASSWORD=models.IntegerField()

     
