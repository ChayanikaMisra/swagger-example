from django.db import models


# Create your models here.


class Showroom(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=70)


class Car(models.Model):
    model_no = models.IntegerField()
    model_name = models.CharField(max_length=70)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
