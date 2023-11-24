from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


'''
class USER_DETAILS(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_lemaength=30)
    password = models.CharField(max_length=30)
    confirm = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username


'''