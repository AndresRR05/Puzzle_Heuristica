from django.urls import path

from django_views import inicio

urlpatterns = [
    path("", inicio, name="inicio"),
]
