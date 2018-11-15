"""Defines URL patterns for learning_logs."""

from django.urls import include, re_path, path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path(r'', views.index, name='index')
]