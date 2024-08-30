from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_test, name='start_test'),  # Start of psychological test
    path('questions/', views.test_questions, name='test_questions'),  # Test questions page
    path('results/', views.test_results, name='test_results'),  # Test results page
]
