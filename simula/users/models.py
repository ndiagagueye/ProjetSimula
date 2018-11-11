from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profession = models.CharField(max_length=100, blank=True, null=True)