from django.shortcuts import render

from django.urls import path, include
from whisper import views
from whisper.models import Whisper

app_name = 'whisper'
urlpatterns = [
    path('', views.WhisperList.as_view(), name='list'),
    path('/test/', views.test, name='test')
]
