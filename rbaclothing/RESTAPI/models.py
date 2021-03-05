from django.db import models

# Create your models here.
class Customer(models.Model):
    Customer_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, default="")
    DateOfBirth = models.DateField()


    def __str__(self):
        return self.Customer_Name