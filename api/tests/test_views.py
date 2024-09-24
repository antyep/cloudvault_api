from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import CustomUser, Media
from api.serializer import CustomUserSerializer, MediaSerializer
from django.core.files.uploadedfile import SimpleUploadedFile


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username='testuser', email='test@example.com', password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

        self.media = Media.objects.create(
            title='Test Media',
            description='Test Description',
            file_size=1024,
            user=self.user,
            is_public=True,
            media_file=SimpleUploadedFile(
                "test.mp4", b"file_content", content_type="video/mp4"),
            file_type='video'
        )

    def test_list_users(self):
        response = self.client.get(reverse('customuser-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(reverse('customuser-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_media(self):
        response = self.client.get(reverse('media-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)

        for idx, item in enumerate(response.data):
            item['media_file'] = item['media_file'].replace(
                'http://testserver', '')
            expected_media_file = serializer.data[idx]['media_file']
            self.assertEqual(item['media_file'], expected_media_file)

    def test_create_media(self):
        media_file = SimpleUploadedFile(
            "file.mp4", b"file_content", content_type="video/mp4"
        )
        data = {
            'title': 'New Media',
            'description': 'New Description',
            'file_size': 2048,
            'user': self.user.id,
            'is_public': True,
            'media_file': media_file,
            'file_type': 'video'
        }
        response = self.client.post(
            reverse('media-list'), data, format='multipart'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
