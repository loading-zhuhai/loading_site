from django.urls import path
from examples import views

urlpatterns = [
    path('', views.joanne_examples, name='joanne_examples'),
]
