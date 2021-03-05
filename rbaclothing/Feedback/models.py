from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class FeedBack(models.Model):
	Name = models.CharField(max_length=20)
	Email = models.EmailField()
	Subject = models.CharField(max_length=20)
	Message = models.TextField()
	img = models.ImageField(upload_to='shop/')

	def __str__(self):
		return self.Name
