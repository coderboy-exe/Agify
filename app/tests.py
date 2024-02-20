from datetime import datetime
import json
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from app.helpers import get_birthyear, compute_details


class HelpersTestCase(TestCase):
    def test_get_birthyear(self):
        age = 30
        expected_birthyear = datetime.now().year - age
        self.assertEqual(get_birthyear(age), expected_birthyear)

    @patch('app.helpers.requests.get')
    def test_compute_details(self, mock_get):
        mock_response = {
            'age': 30
        }
        mock_get.return_value.status_code = status.HTTP_200_OK
        mock_get.return_value.text = json.dumps(mock_response)
        
        name = 'John'
        result = compute_details(name)
        expected_birthyear = datetime.now().year - mock_response['age']
        
        self.assertEqual(result['name'], name)
        self.assertEqual(result['age'], mock_response['age'])
        self.assertEqual(result['date_of_birth'], expected_birthyear)


class AgeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_age_invalid_request(self):
        url = reverse('get_age')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_age_invalid_name(self):
        url = reverse('get_age')
        data = {'name': 123}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('app.views.compute_details')
    def test_get_age_cached(self, mock_compute_details):
        name = 'John'
        mock_response = {'name': name, 'age': 30, 'date_of_birth': datetime.now().year - 30}
        mock_compute_details.return_value = mock_response
        
        url = reverse('get_age')
        data = {'name': name}
        
        # First call, not cached
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, mock_response)
        
        # Second call, cached
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, mock_response)
