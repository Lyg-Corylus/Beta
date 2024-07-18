"""
URL configuration for corylus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from api.Login.login_view import login_sesion, generate_token_view
from api.home.home_view import home,home_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('login/', login_sesion,name='login'),
    path('generate_token/', generate_token_view, name='generate_token'),
    path('', home,name='home'),
    path('home_token/', home_token,name='home_token'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
