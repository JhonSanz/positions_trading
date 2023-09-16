from rest_framework import serializers
from position.models import Position
from position.serializers.asset import AssetSerializer


class PositionSerializer(serializers.ModelSerializer):
    order_type_display = serializers.CharField(source='get_order_type_display')
    direction_display = serializers.CharField(source='get_direction_display')
    asset = AssetSerializer()

    class Meta:
        model = Position
        fields = [
            'id', 'created_at', 'updated_at', 'open_date',
            'reference', 'direction', 'direction_display',
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
