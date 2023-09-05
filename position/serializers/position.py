from rest_framework import serializers
from position.models import Position


class PositionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Position
		fields = ['id', 'created_at', 'updated_at', 'open_date', 'close_date', 'price', 'volume', 'leverage', 'order_type', 'asset']


class PositionCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Position
		fields = ['id', 'created_at', 'updated_at', 'open_date', 'close_date', 'price', 'volume', 'leverage', 'order_type', 'asset']
