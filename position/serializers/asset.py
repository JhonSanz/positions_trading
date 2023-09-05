from rest_framework import serializers
from position.models import Asset


class AssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ['position', 'id', 'created_at', 'updated_at', 'name', 'presition', 'swap_coeficient', 'broker']


class AssetCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ['position', 'id', 'created_at', 'updated_at', 'name', 'presition', 'swap_coeficient', 'broker']
