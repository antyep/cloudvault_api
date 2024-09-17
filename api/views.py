import os
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from rest_framework import viewsets
from .models import Task, Tag
from .serializer import TaskSerializer, TagSerializer
from socket import gethostbyname
from socket import gethostname

# Create your views here.


def index(request):

    subject = "API Verification"
    recipient_list = ['delirevered@resend.dev']
    from_email = 'onboarding@resend.dev'
    message = 'Hello, hope you are doing great.'

    with get_connection(
        host=settings.RESEND_SMTP_HOST,
        port=settings.RESENT_SMTP_PORT,
        username=settings.RESEND_SMTP_USERNAME,
        password=os.environ["RESEND_API_KEY"],
        use_tls=True,
    ) as connection:
        r = EmailMessage(
            subject=subject,
            body=message,
            to=recipient_list,
            from_email=from_email,
            connection=connection).send()
    return JsonResponse({'status': 'ok'})


class TaskViewSet (viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
