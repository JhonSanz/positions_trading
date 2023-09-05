from rest_framework import serializers
from position.models import Broker


class BrokerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Broker
		fields = ['account', 'asset', 'id', 'created_at', 'updated_at', 'name', 'website']


class BrokerCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Broker
		fields = ['account', 'asset', 'id', 'created_at', 'updated_at', 'name', 'website']
