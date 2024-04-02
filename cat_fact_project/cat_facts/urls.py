from django.urls import path
from . import views

urlpatterns = [
    path('health_check/', views.health_check, name='health_check'),
    path('fetch_fact/', views.fetch_fact, name='fetch_fact'),
    path('get_fact/', views.get_fact, name='get_fact'),
]
