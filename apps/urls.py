from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_apps, name="apps"),
    path('<int:id>', views.get_app ),
    path('new', views.create_app, name="create_app")
]

