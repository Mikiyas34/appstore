
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register")
] 