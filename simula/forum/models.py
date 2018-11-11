from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    publish = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/", null=True, blank=True)

    def __str__(self):
        return self.body[:30]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    note = models.IntegerField(default=0)
    validate = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:30]


class Response(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.TextField()
