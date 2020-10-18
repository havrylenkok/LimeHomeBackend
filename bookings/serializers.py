from rest_framework import serializers

from bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'date_created', 'date_changed', 'property_id']

    def validate_property_id(self, value):
        # It is not permissible to use URL templating. Please follow the Places API Developer Guide:
        # https://developer.here.com/rest-apis/documentation/places/topics/required-user-flow.html
        # >Unfortunately, the page you're looking for doesn't seem to exist. ¯\_(ツ)_/¯
        # response = requests.get(f'https://places.ls.hereapi.com/places/v1/places/{value}/',
        #              dict(apiKey=HERE_API_KEY))
        # if not response:
        #     raise serializers.ValidationError("Property does not exist")
        return value
