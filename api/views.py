from rest_framework import viewsets
from .models import Task, Tag
from .serializer import TaskSerializer, TagSerializer

# Create your views here.


class TaskViewSet (viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
