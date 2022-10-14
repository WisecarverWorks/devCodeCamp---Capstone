from django.db import models
from authentication.models import User
# Create your models here.

class Bulletin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100, default = None)
    overview = models.TextField(max_length = None, default = None)
    # every model must have an __init__ method