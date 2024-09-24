from django.test import TestCase
from api.models import CustomUser, Media
from api.serializer import CustomUserSerializer, MediaSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os


class SerializerTest(TestCase):

    def setUp(self):
        self.custom_user_data = {
            'username': 'testuser',
            'email': 'media_user@example.com',
            'password': 'password123'
        }
        self.custom_user = CustomUser.objects.create(**self.custom_user_data)

    def test_custom_user_serialization(self):
        serializer = CustomUserSerializer(self.custom_user)
        self.assertEqual(
            serializer.data['username'], self.custom_user_data['username'])
        self.assertEqual(serializer.data['email'],
                         self.custom_user_data['email'])


class MediaSerializerTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username='media_user',
            email='media_user@example.com',
            password='password123'
        )
        self.media_file = SimpleUploadedFile(
            "test.mp4", b"file_content", content_type="video/mp4")
        self.media_data = {
            'title': 'Test Media',
            'description': 'This is a test description.',
            'media_file': self.media_file,
            'file_size': 123,
            'user': self.user,
            'is_public': True,
            'is_deleted': False,
        }
        self.media = Media.objects.create(**self.media_data)

    def test_media_serialization(self):
        serializer = MediaSerializer(self.media)
        self.assertEqual(serializer.data['title'], self.media_data['title'])

        relative_path = self.media.media_file.name

        expected_full_path = os.path.join(
            settings.MEDIA_URL, relative_path).replace('\\', '/')

        expected_full_path = expected_full_path.replace('//', '/')

        self.assertEqual(serializer.data['media_file'], expected_full_path)

    def test_media_deserialization(self):
        serializer_data = {
            'title': 'Test Media',
            'description': 'This is a test description.',
            'media_file': self.media_file,
            'file_size': 123,
            'user': self.user.id,
            'is_public': True,
            'is_deleted': False,
            'file_type': 'video/mp4',
        }
        serializer = MediaSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid(),
                        msg=f"Errors: {serializer.errors}")
        self.assertEqual(
            serializer.validated_data['title'], serializer_data['title'])
