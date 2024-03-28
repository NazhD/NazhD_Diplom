from django.db import models
from django.contrib.auth.models import User


class UserPage(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, default="user")
    topic = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='profiles/images/', default="profiles/astartes1.png")



