from rest_framework import serializers
from position.models import Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            "id", "ticker", "quantity", "price",
            "date", "user", "broker"
        ]
