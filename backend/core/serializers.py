from dataclasses import fields
from rest_framework import serializers
from .models import *

# class GetAllInformationSerializer(serializers.ModelSerializer):
#     """Get all information for a feature."""
#     class Meta: 
#         model = FullInformation
#         fields = '__all__'
# 
class FeatureSerializer(serializers.ModelSerializer):
   class Meta:
    model = Feature
    fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = 'id', 'user', 'created_by', 'created_at', 'updated_at', 'review', 'rating'
        depth = 1
        
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = 'id', 'feature', 'created_by', 'created_at', 'updated_at', 'log'
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id', 'feature', 'created_by', 'created_at', 'updated_at', 'comment'
        depth = 1

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = 'id', 'feature', 'created_by', 'created_at', 'updated_at', 'artwork'
        depth = 1

class FullInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullInformation
        fields = 'id', 'feature', 'created_by', 'created_at', 'updated_at', 'artwork', 'log', 'comment', 'review', 'rating'
        depth = 1
        
# Path: core/services.py