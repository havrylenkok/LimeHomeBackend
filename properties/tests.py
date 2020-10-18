import json

import httpretty as httpretty
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from limehometest.settings import HERE_API_KEY, HERE_PLACES_BASE_URL
from bookings.serializers import BookingSerializer
from properties.serializers import PropertySerializer, PropertyQuerySerializer


class ApiPropertyBookingsListViewTestCase(APITestCase):
    def setUp(self):
        self.property_id = 'qwe'
        self.booking = mommy.make('bookings.Booking', property_id=self.property_id)

    def test_list_property_bookings(self):
        url = reverse("properties:bookings", args=[self.property_id])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'], [BookingSerializer(self.booking).data])

        url = reverse("properties:bookings", args=['asd'])
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.data['results'], [])


class ApiPropertyListViewTestCase(APITestCase):

    def setUp(self):
        pass

    @httpretty.activate
    def test_list_properties(self):
        body_str = b'{"results":{"items":[{"position":[52.510398,13.38857],"distance":874,"title":"NH Collection Berlin Mitte am Checkpoint Charlie","averageRating":0.0,"category":{"id":"hotel","title":"Hotel","href":"href","type":"urn:nlp-types:category","system":"places"},"icon":"icon","vicinity":"Leipziger Stra\xc3\x9fe 106<br/>Mitte, 10117 Berlin","having":[],"type":"urn:nlp-types:place","href":"href", "id":"id"}]}}'
        body = json.loads(body_str)
        uri = f'{HERE_PLACES_BASE_URL}discover/explore/?at=52.5039563%2C13.3959692&cat=accommodation&apiKey={HERE_API_KEY}'
        httpretty.register_uri(
            httpretty.GET,
            uri,
            body=body_str
        )
        url = f'{reverse("properties:index")}?at=52.5039563,13.3959692'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, PropertySerializer(body.get('results').get('items'), many=True).data)


class PropertyQuerySerializerTestCase(APITestCase):

    def setUp(self):
        pass

    def test_positive(self):
        data = dict(at='1.0,2.0')
        serializer = PropertyQuerySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_validate_at(self):
        data = dict(at='1.02.0')
        serializer = PropertyQuerySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertTrue('at' in serializer.errors)

        data = dict(at='1.0,qqq')
        serializer = PropertyQuerySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertTrue('at' in serializer.errors)
