from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'CustomUser', views.CustomUserViewSet)
router.register(r'Media', views.MediaViewSet)

urlpatterns = router.urls
