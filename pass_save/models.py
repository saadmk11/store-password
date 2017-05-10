from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pass(models.Model):
	user = models.ForeignKey(User)
	account_name = models.CharField(max_length=30)
	user_name = models.CharField(max_length=20)
	password = models.CharField(max_length=30)

	def __str__(self):              
		return self.account_name