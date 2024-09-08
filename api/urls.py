from django.urls import path
from rest_framework import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'tags', views.TagViewSet)
