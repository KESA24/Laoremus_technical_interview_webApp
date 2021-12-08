from django.db import models

#Create your models here.

TASTE_CHOICES = (
    ('HIGHQUALITY', '1'),
    ('AVERAGE', '2'),
    ('BELOWAVERAGE','3')

)

SMELL_CHOICES = (
    ('HIGHQUALITY', '1'),
    ('AVERAGE', '2'),
    ('BELOWAVERAGE','3')

)

DELIVER_CHOICES = (
    ('HIGHQUALITY', '1'),
    ('AVERAGE', '2'),
    ('BELOWAVERAGE','3')
)

ADULTERATION_CHOICES = (
    ('NONE', '1'),
    ('LOW', '2'),
    ('HIGH','3')
)

class Farmer(models.Model):
    names = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    village = models.CharField(max_length=1000)
    nin = models.CharField(max_length=1000)
    cows= models.CharField(max_length=1000)

    def __str__(self):
        return self.names , self.phone , self.village, self.cows , self.nin

class Milk(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.IntegerField()
    taste = models.CharField(choices=TASTE_CHOICES, max_length=100)
    smell = models.CharField(choices= SMELL_CHOICES, max_length=100)
    delivery = models.CharField(choices=DELIVER_CHOICES, max_length=100 )
    adulteration = models.CharField(choices=ADULTERATION_CHOICES, max_length=100)

    def __str__(self):
        return self.date, self.time, self.amount, self.taste, self.smell, self.delivery, self.adulteration