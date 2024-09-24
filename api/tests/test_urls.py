from django.test import TestCase
from django.urls import reverse, resolve
from api.views import CustomUserViewSet, MediaViewSet


class UrlsTestCase(TestCase):
    def test_customuser_list_url(self):
        url = reverse('customuser-list')
        self.assertEqual(resolve(url).func.__name__,
                         CustomUserViewSet.as_view({'get': 'list'}).__name__)

    def test_customuser_detail_url(self):
        url = reverse('customuser-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__,
                         CustomUserViewSet.as_view({'get': 'retrieve'}).__name__)

    def test_media_list_url(self):
        url = reverse('media-list')
        self.assertEqual(resolve(url).func.__name__,
                         MediaViewSet.as_view({'get': 'list'}).__name__)

    def test_media_detail_url(self):
        url = reverse('media-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.__name__,
                         MediaViewSet.as_view({'get': 'retrieve'}).__name__)

    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(url, '/admin/')

    def test_api_docs_url(self):
        url = '/docs/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_allauth_urls(self):
        allauth_urls = [
            'account_login',
            'account_logout',
            'account_inactive',
            'account_signup',
            'account_email',
            'account_change_password',
            'account_set_password',
            'account_reset_password',
            'account_reset_password_done',
        ]
        for url_name in allauth_urls:
            url = reverse(url_name)
            self.assertTrue(url.startswith('/accounts/'))

        url = reverse('account_confirm_email', kwargs={'key': 'testkey'})
        self.assertTrue(url.startswith('/accounts/confirm-email/'))
