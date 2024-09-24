from django.test import TestCase
from api.models import CustomUser, Media


class MediaModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.media = Media.objects.create(
            title='Test Media',
            user=self.user,
            media_file='media/testfile.jpg',
            file_type='image/jpeg',
            file_size=1000
        )

    def test_media_creation(self):
        self.assertEqual(self.media.title, 'Test Media')
        self.assertEqual(self.media.user, self.user)

    def test_str_representation(self):
        self.assertEqual(str(self.media), 'Test Media')
