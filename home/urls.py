from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='profile'),
    path('', views.home, name='points'),
    path('', views.home, name='tasks'),
    path('apps', views.create_app, name='apps'),
]