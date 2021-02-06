from django.urls import path
from joanne import views

urlpatterns = [
    path('', views.joanne, name='joanne'),
]
