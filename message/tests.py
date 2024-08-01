from django.test import SimpleTestCase
from django.urls import reverse

class TestMessage(SimpleTestCase):
    def test_url_exists_by_path(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_by_name(self):
        url = reverse('message')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_template_name(self):
        url = reverse('message')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
    def test_content (self):
        url = reverse('message')
        response = self.client.get(url)
        self.assertContains(response,'<h1>Hello User</h1>')