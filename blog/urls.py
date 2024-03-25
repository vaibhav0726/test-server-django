from django.urls import path

from . import views

urlpatterns = [
    path("response", views.index, name="index"),
    path("", views.blog, name="blog"),
]