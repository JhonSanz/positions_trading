from rest_framework import serializers
from position.models import Position
from position.serializers.asset import AssetSerializerMini


class PositionSerializer(serializers.ModelSerializer):
    order_type_display = serializers.CharField(source='get_order_type_display')
    direction_display = serializers.CharField(source='get_direction_display')
    asset = AssetSerializerMini()

    class Meta:
        model = Position
        fields = [
            'id', 'open_date',
            'reference', 'direction', 'direction_display',
            'close_date', 'price', 'volume', 'is_leveraged',
            'order_type', 'order_type_display', 'asset', 'description'
        ]


class PositionSerializer(PositionSerializer):
    subpositions = PositionSerializer(source="get_sub_positions", many=True)

    class Meta:
        model = Position
        fields = PositionSerializer.Meta.fields + ['subpositions']


class PositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'reference', 'open_date', 'close_date', 'price', 'volume',
            'order_type', 'direction', 'asset', 'is_leveraged',
        ]
