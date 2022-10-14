from django.urls import path, include
from bulletin import views

urlpatterns = [
    path('', views.get_bulletin),

]
