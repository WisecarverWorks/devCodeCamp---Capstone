from django.urls import path, include
from work import views

urlpatterns = [
    path('', views.get_work),
    path('<pk>/', views.user_work),
]
