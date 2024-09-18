from rest_framework import viewsets
from .models import CustomUser, Media
from .serializer import CustomUserSerializer, MediaSerializer

# Create your views here.


class CustomUserViewSet (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
