from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiBookingCreateViewTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_booking(self):
        url = reverse("bookings:create")
        data = dict(property_id='test')
        response = self.client.post(url, data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['property_id'], data['property_id'])
