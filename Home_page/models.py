from django.db import models

# Create your models here.


class ITEMDATABASE(models.Model):

    img = models.ImageField(upload_to='pics')
    oldness = models.CharField(max_length=15)
    item = models.CharField(max_length=15)
    price = models.IntegerField(default=0)