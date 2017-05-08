from django.db import models

# Create your models here.
class Pass(models.Model):
	account_name = models.CharField(max_length=30)
	user_name = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

	def __str__(self):              
		return self.account_name