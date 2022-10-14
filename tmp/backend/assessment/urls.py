from django.urls import path, include
from assessment import views

urlpatterns = [
    path('', views.assessment)
]