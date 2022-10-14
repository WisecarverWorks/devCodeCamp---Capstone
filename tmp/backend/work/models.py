from django.db import models
from authentication.models import User
# Create your models here.


class Work(models.Model):
    #fields:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_note = models.CharField(max_length=100)

    user_assessment = models.CharField(max_length=25)
