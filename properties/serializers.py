from decimal import Decimal, InvalidOperation

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PropertyQuerySerializer(serializers.Serializer):
    at = serializers.CharField()

    def validate_at(self, at):
        if ',' not in at:
            raise ValidationError('Did not supply coordinates')
        else:
            lat, long = at.split(',')
            try:
                lat = Decimal(lat)
                long = Decimal(long)
            except InvalidOperation:
                raise ValidationError('Did not supply coordinates')
        return at


class PropertySerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    position = serializers.ListField(child=serializers.DecimalField(max_digits=9, decimal_places=6))
    averageRating = serializers.FloatField()
    vicinity = serializers.CharField()
    type = serializers.CharField()
    icon = serializers.CharField()
    href = serializers.CharField()
    category = serializers.DictField(child=serializers.CharField())
    distance = serializers.IntegerField()
    openingHours = serializers.DictField(child=serializers.CharField(), required=False)
    chainIds = serializers.ListField(child=serializers.CharField(), required=False)
    alternativeNames = serializers.ListField(child=serializers.DictField(child=serializers.CharField()), required=False)
