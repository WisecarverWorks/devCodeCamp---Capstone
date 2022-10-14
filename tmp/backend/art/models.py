from django.db import models
from authentication.models import User

# Create your models here.

class Art(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=200)

    artwork_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    artwork_group = models.CharField(max_length=50)
    artwork_collection = models.CharField(max_length=100)

    artwork_name = models.CharField(max_length=100)
    artwork_description = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.IntegerField()
    in_stock = models.BooleanField(default=True)