from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Art),
    path('all/', views.get_all_art),
]