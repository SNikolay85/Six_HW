from unittest import TestCase
from rest_framework.test import APIClient


class TestView(TestCase):
    def test(self):
        url = '/api/v1/test/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'Test CICD all')
