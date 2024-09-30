from rest_framework import viewsets
from .models import CustomUser, Media
from .serializer import CustomUserSerializer, MediaSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializer import LoginSerializer

# Create your views here.


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.create(serializer.validated_data)
            return Response(user_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserViewSet (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
