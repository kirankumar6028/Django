from django.db import models

# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
