from django.urls import path
from mo import views

urlpatterns = [
    path('', views.mo, name='mo'),
]
