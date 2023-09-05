from rest_framework import serializers
from position.models import Money


class MoneySerializer(serializers.ModelSerializer):
	class Meta:
		model = Money
		fields = ['accountmoney', 'id', 'created_at', 'updated_at', 'currency']


class MoneyCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Money
		fields = ['accountmoney', 'id', 'created_at', 'updated_at', 'currency']
