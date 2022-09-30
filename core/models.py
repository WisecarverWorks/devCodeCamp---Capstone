# Models in this file will represent Features in the applications user stories.
from datetime import date
from enum import auto
from tkinter import CASCADE
from django.db import models
from django.forms import DateField, DateTimeField
from authentication.models import User

class Feature(models.Model):
    """A feature is a user story that is being worked on by the team."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
    
class Assessment(models.Model):
    """An assessment is a review of a feature by a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.review
    
class Log(models.Model):
    """A log is a record of a feature's progress."""
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    log = models.TextField()

    def __str__(self):
        return self.log
    
class Comment(models.Model):
    """A comment is a note on a feature."""
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment
    
class Artwork(models.Model):
    """An artwork is a visual representation of a feature."""
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artwork = models.ImageField()

    def __str__(self):
        return self.artwork

class FullInformation(models.Model):
    """Full information is a collection of all information for a feature."""
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artwork = models.ImageField()
    log = models.TextField()
    comment = models.TextField()
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.feature
    
# Path: core/models.py