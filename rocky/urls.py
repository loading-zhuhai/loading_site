from django.urls import path
from rocky import views

urlpatterns = [
    path('', views.rocky, name='rocky'),
]

