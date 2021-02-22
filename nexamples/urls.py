
from django.urls import path
from nexamples import views

urlpatterns = [
    path('', views.nexamples, name='nexamples'),
]
