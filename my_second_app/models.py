from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(
        max_length=128
    )
    price = models.IntegerField(
        default=0
    )



