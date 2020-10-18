from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets
from rest_framework.response import Response

from bookings.models import Booking
from bookings.serializers import BookingSerializer
from properties.serializers import PropertySerializer, PropertyQuerySerializer
from utils.here_places import HerePlacesApi


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
            api = HerePlacesApi()
            places = api.near_coordinates(query_serializer.validated_data["at"])
        serializer = PropertySerializer(instance=places, many=True)
        return Response(serializer.data)


class ApiPropertyBookingsListView(generics.ListAPIView):
    """
    API endpoint to list Property Bookings
    """
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(property_id=self.kwargs['id'])
