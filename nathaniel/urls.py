from django.urls import path
from nathaniel import views

urlpatterns = [
    path('', views.nathaniel, name='nathaniel'),
]
