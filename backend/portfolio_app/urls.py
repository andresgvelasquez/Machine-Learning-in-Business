from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_files, name='upload_file'),
    path('success/', views.success, name='success'),
    path('api/correlation-matrix/', views.get_correlation_matrix, name='correlation_matrix'),
    #path('', views.home, name='home'),
]