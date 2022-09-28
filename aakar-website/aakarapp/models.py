from django.db import models


# Create your models here.

class TaskZero(models.Model):
    crid = models.CharField(max_length=10)
    username = models.CharField(max_length = 200)
    colgName = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    mobileNo = models.CharField(max_length=10)
    dept = models.CharField(max_length = 200)
    whatsappNo = models.CharField(max_length = 200)
    pincode = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    

    def __str__(self):
        return (
            f"{self.username} "
            f"{self.crid} "
            f"{self.colgName} "
            f"{self.state} "
            f"{self.mobileNo} "
            f"{self.whatsappNo} "
            f"{self.address} "
            f"{self.pincode} "
            f"{self.dept} "
        )
    



