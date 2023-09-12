from rest_framework import serializers
from position.models import Position


class PositionSerializer(serializers.ModelSerializer):
    order_type_display = serializers.CharField(source='get_order_type_display')

    class Meta:
        model = Position
        fields = [
            'id', 'created_at', 'updated_at', 'open_date',
            'reference', 'direction',
            'close_date', 'price', 'volume', 'is_leveraged',
            'order_type', 'order_type_display', 'asset'
        ]


class PositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'reference', 'open_date', 'close_date', 'price', 'volume',
            'is_leveraged', 'order_type', 'asset', 'direction'
        ]
