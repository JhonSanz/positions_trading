from django.db.models import Sum, F
from rest_framework import serializers
from position.models import Position
from position.serializers.asset import AssetSerializerMini
from utilities.constant import LONG


class PositionSerializer(serializers.ModelSerializer):
    order_type_display = serializers.CharField(source='get_order_type_display')
    direction_display = serializers.CharField(source='get_direction_display')
    asset = AssetSerializerMini()
    open_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    close_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    benefit = serializers.SerializerMethodField()

    class Meta:
        model = Position
        fields = [
            'id', 'open_date',
            'reference', 'direction', 'direction_display',
            'close_date', 'price', 'volume', 'is_leveraged',
            'order_type', 'order_type_display', 'asset', 'description',
            'benefit'
        ]
    
    def get_benefit(self, obj):
        result = (obj.price * obj.volume) - (obj.reference.price * obj.volume)
        return result if obj.reference.order_type == LONG else result * -1


class PositionSerializer(PositionSerializer):
    subpositions = PositionSerializer(source="get_sub_positions", many=True)

    class Meta:
        model = Position
        fields = PositionSerializer.Meta.fields + ['subpositions']

    def get_benefit(self, obj):
        result =  Position.objects.filter(reference=obj).aggregate(
            benefit=Sum(F("volume") * (F("price") - obj.price))
        ).get("benefit")
        return result if obj.order_type == LONG else result * -1

class PositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'reference', 'open_date', 'close_date', 'price', 'volume',
            'order_type', 'direction', 'asset', 'is_leveraged',
            'description'
        ]
