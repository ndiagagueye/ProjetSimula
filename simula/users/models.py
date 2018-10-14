from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
	name = models.CharField(max_length=100, verbose_name="Nom complet")
	user = models.OneToOneField(User, on_delete=models.CASCADE)