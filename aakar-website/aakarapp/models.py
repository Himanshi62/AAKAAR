from django.db import models


# Create your models here.

class TaskZero(models.Model):
    crid = models.CharField(max_length=10)
    firstName = models.CharField(max_length = 200)
    lasttName = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return (
            f"{self.firstName} "
            f"{self.crid} "
            f"{self.lasttName} "
            f"{self.city} "
            f"{self.phone} "
        )
    



