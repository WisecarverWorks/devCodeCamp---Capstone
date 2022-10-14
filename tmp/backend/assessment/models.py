from django.db import models
from authentication.models import User

# Create your models here.

class Assessment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  title = models.CharField(max_length = 100, default = "title")

  overview = models.TextField(max_length=None, default="overview")

  rating = models.IntegerField()
  