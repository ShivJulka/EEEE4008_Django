"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from .views import homePage
from .views import Registration
from .views import LogIn
from .views import profile_view
from .views import edit_profile


urlpatterns = [
    path('',homePage), #home
    path('Registration/',Registration), #log in function
    path('admin/', admin.site.urls),
    path('LogIn/', LogIn, name="login"),  # log in function
    path('profile/', profile_view, name="profile"),  # log in function
    path('profile/', edit_profile, name="edit_profile"),  # log in function

]
