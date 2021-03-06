"""loading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('landing_page.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('about/', include('about.urls')),
    path('team/', include('team.urls')),    
    path('news/', include('news.urls')),
    path('contact/', include('contact.urls')),
    path('team/joanne/', include('joanne.urls')),
    path('team/nathaniel/', include('nathaniel.urls')),
    path('team/mo/', include('mo.urls')),
    path('team/rocky/', include('rocky.urls')),
    path('examples/joanne/', include('examples.urls')),
    path('examples/nate/', include('nexamples.urls')),

]
