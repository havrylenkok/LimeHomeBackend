from rest_framework import generics

#
from bookings.models import Booking
from bookings.serializers import BookingSerializer


class ApiBookingCreateView(generics.CreateAPIView):
    """
    API endpoint to create Bookings
    """
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
