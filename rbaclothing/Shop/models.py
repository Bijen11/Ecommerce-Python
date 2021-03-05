from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
	Product_Id = models.AutoField
	Product_Name = models.CharField(max_length=100)
	Product_Price = models.IntegerField(default=0)
	Product_Description = models.TextField()
	Publication_Date = models.DateField()
	Product_Category = models.CharField(max_length=100, default="")
	Product_Image = models.ImageField(upload_to='shop/images', default="")


	def __str__(self):
		return self.Product_Name

#add to cart customerid is a django user models user id
class OrderItem(models.Model):
	Customer_Id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
	    return f"{self.quantity} of {self.item.Product_Name}"

	def totalprice(self):
		return self.quantity * self.item.Product_Price