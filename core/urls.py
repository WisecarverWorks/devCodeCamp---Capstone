from django.urls import path
from core import views

urlpatterns = [
    path('', views.appIndex, name='index'),
    path('artworks/', views.get_all_assessments),
    path('logs/', views.get_all_logs),
    path('features/', views.get_all_features),
    path('information/', views.get_all_information_by_id),
    path('create-assessment/', views.create_assessment),
    path('create-log/', views.create_log),
    path('create-feature/', views.create_feature),
    path('create-artwork/', views.create_artwork),
]

# Path: core/serializers.py