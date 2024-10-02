from rest_framework import viewsets
from .models import CustomUser, Media
from .serializer import CustomUserSerializer, MediaSerializer
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
import os

# Create your views here.


def index(request):

    subject = "CloudVault Validation"
    recipient_list = ["delivered@resend.dev"]
    from_email = "onboarding@resend.dev"
    message = "<strong>test</strong>"

    with get_connection(
        host=settings.RESEND_SMTP_HOST,
        port=settings.RESEND_SMTP_PORT,
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
        return JsonResponse({"status": "ok"})


class CustomUserViewSet (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
