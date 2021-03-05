from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Invoice(models.Model):
    shipping_address=models.CharField(max_length=100)
    Amount=models.IntegerField(default=0)
    Contact=models.IntegerField()
    Customer_Id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __int__(self):
        return self.Cus_bal