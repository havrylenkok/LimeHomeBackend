import json

import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response

from bookings.models import Booking
from bookings.serializers import BookingSerializer
from limehometest.settings import HERE_API_KEY, HERE_PLACES_BASE_URL
from properties.serializers import PropertySerializer, PropertyQuerySerializer


class ApiPropertyListView(viewsets.ViewSet):
    """
    API endpoint to list Properties
    """
    serializer_class = PropertySerializer

    @swagger_auto_schema(query_serializer=PropertyQuerySerializer, responses={200: PropertySerializer(many=True)})
    def list(self, request):
        query_serializer = PropertyQuerySerializer(data=request.GET)
        places = []
        if query_serializer.is_valid():
            response = requests.get(f'{HERE_PLACES_BASE_URL}discover/explore/',
                                    dict(at=query_serializer.validated_data["at"],
                                         cat='accommodation',
                                         apiKey=HERE_API_KEY))
            data = json.loads(response.content)
            places = data.get('results', {}).get('items', [])
        serializer = PropertySerializer(instance=places, many=True)
        return Response(serializer.data)


class ApiPropertyBookingsListView(generics.ListAPIView):
    """
    API endpoint to list Property Bookings
    """
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(property_id=self.kwargs['id'])
