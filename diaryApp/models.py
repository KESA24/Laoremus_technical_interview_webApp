from django.db import models

# Create your models here.

class Farmer(models.Model):
    names = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    village = models.CharField(max_length=1000)
    nin = models.CharField(max_length=1000)
    cows= models.CharField(max_length=1000)

    def __str__(self):
        return self.names , self.phone , self.village, self.cows , self.nin